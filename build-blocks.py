#!/usr/bin/env python
# -*- coding: utf-8
# Render the contents for each block section in the specified
# project directory. Example: ./build-blocks.py 1A

from os import path, listdir, stat, walk
from sys import argv
from runpy import run_path
import bdf2tikz.main, bdf2tikz.render

def escape(t):
  return bdf2tikz.render.render_tikz_text(t, {})

def get(o, n, d):
  if n in o: return o[n]
  return d

def splitext(n):
  dirname, basename = path.split(n)
  name, ext = path.splitext(basename)
  return (n, name, ext)

project = argv[1]
pdir = path.join(path.dirname(__file__), project)
bdir = path.join(pdir, "blocks")
adir = path.join(pdir, "assets")
simulations = []
if path.isdir(path.join(adir, "vwf")):
  simulations = map(splitext, listdir(path.join(adir, "vwf")))

def get_simulation_files(name, block):
  # Search for exact match
  matches = filter(lambda x: x[1] == name, simulations)
  if len(matches):
    if len(matches) >= 2: print "WARNING: Multiple matches: %s" % matches
    return [matches[0][0]]

  # Search for partial matches
  def filter_func(n):
    n, fname, ext = n
    idx = fname.rfind("--")
    if idx == -1: return False
    return name == fname[:idx]
  matches = filter(filter_func, simulations)
  return map(lambda x: x[0], matches)

def render_block(name, block, imported=False):
  output = [unicode()]
  def put(s, *k):
    assert(s.startswith(u"\n"))
    while s.endswith(u" "): s = s[:-1]
    s = s[1:]
    if len(k) != 0: s = s % tuple(k)
    output[0] += s

  # Labeled subsection
  put(ur'''
\subsection{\label{sub:\projectname-%s} \textsf{%s}}

  ''', name, escape(name))

  # Symbol
  if not get(block, "top_level", False):
    put(ur'''
\paragraph{Símbol}

\begin{center} \bsfsymbol{%s} \end{center}

    ''', name)

  # Ports
  def render_port(t):
    name, direction, desc = t
    name = bdf2tikz.render.render_node_name(name, bdf2tikz.main.default_options)[1:-1]
    return u"\item[%s] %s" % (name, desc.strip())
  ports = map(render_port, get(block, "ports", []))
  if len(ports):
    ports = u"\\begin{where}\n%s\n\\end{where}" % "\n".join(ports)
  else:
    ports = "% FIXME\nNo hi ha ports definits."
  put(ur'''
\paragraph{Entrades i sortides}

%s

  ''', ports)

  # Description
  description = get(block, "description", u"% FIXME\nSense descripció.")
  put(ur'''
\paragraph{Funció}

%s

  ''', description.strip())

  # Unspecifications
  unspecs = get(block, "unspecs", u"Cap.")
  put(ur'''
\paragraph{Inespecificacions}

%s

  ''', unspecs)

  # Notes
  notes = get(block, "notes", [])
  if len(notes):
    put(ur'''
\paragraph{Notes}

%s

    ''', u"\n\n".join(map(unicode.strip, notes)))

  # Schematic / VHDL and implementation
  if not imported:
    put(ur'''
\paragraph{Implementació}

    ''')

    vhd_exists = path.isfile(path.join(adir, "vhdl", name + ".vhd"))
    bdf_exists = path.isfile(path.join(adir, "schematics", name + ".tex"))
    if vhd_exists == bdf_exists: print "WARNING: Wrong assets for %s" % name
    intro_text = unicode()

    if vhd_exists:
      put(ur'''
\vhdlisting{%s}

      ''', name)

    if bdf_exists:
      ref = u"fig:sch-\\projectname-%s" % name
      put(ur'''
\begin{contendfig}
  \begin{center}
    \adjustbox{max width=\textwidth, max height=\textheight}{
      \bdfschematic{%s}
    }
  \end{center}
  \caption{\label{%s} Esquemàtic per al bloc \textsf{%s}}
\end{contendfig}

      ''', name, ref, escape(name))
      intro_text += u"L'esquemàtic del bloc es pot veure a la figura~\\ref{%s} (pàgina~\\pageref{%s}). " % (ref, ref)

    implementation = get(block, "implementation", "% FIXME")
    put(ur'''
%s

%s

    ''', intro_text.strip(), implementation.strip())

  # Simulation
  simulation = get(block, "simulation", u"").strip()
  sim_files = get_simulation_files(name, block)
  if (not imported) and (len(sim_files) or len(simulation)):
    assert len(sim_files)
    ref = u"fig:sim-\\projectname-%s" % name
    render_sim = lambda s: u"\includegraphics[scale=0.55]{../\\projectname/assets/vwf/%s}" % s
    sim_files = u"\n\n\\vspace{1em}\n\n".join(map(render_sim, sim_files))
    put(ur'''
\paragraph{Simulació}

\begin{contendfig}
  \begin{center}
    %s
  \end{center}
  \caption{\label{%s} Simulació per al bloc \textsf{%s}}
\end{contendfig}

La simulació del bloc es pot veure a la figura~\ref{%s} (pàgina~\pageref{%s}).

%s

  ''', sim_files, ref, escape(name), ref, ref, simulation or "% FIXME")

  put(ur'''
\vspace{1cm}
  ''')
  return output[0]


def process_file(dirname, block):
  name, ext = path.splitext(basename)
  if ext != ".py": return
  block = run_path(path.join(dirname, block))
  output = render_block(name, block, path.split(dirname)[1] == "imported")
  file = open(path.join(dirname, name + ".tex"), "w")
  file.write(output.encode("utf-8"))
  file.close()

for dirname, dirnames, basenames in walk(bdir):
  for basename in basenames:
    process_file(dirname, basename)
