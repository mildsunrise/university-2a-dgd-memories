#!/usr/bin/env python
# -*- coding: utf-8
# Render the contents for each block section in the specified
# project directory. Example: ./build-blocks.py 1A

from os import path, listdir, stat, walk
from sys import argv
from runpy import run_path
from bdf2tikz import bdf2tikz
from vwf2tikz import vwf2tikz

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
simulations = {}
for dirname, dirnames, basenames in walk(pdir):
  for basename in basenames:
    name, ext = path.splitext(basename)
    if ext != ".vwf": continue
    idx = name.rfind("--")
    if idx != -1: name = name[:idx]
    if name not in simulations: simulations[name] = []
    simulations[name].append(path.join(dirname, basename))

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
    name = bdf2tikz.render.render_node_name(name, bdf2tikz.process.default_options)[1:-1]
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
  sim_files = sorted(simulations[name] if name in simulations else [])
  timings = get(block, "timings", None)
  if timings is None:
    timings = [{ "slices": [(0,100000)] }] * len(sim_files)
  if len(sim_files) != len(timings):
    print "WARNING: found %d simulations, %d specified" % (len(sim_files), len(timings))

  simulation = get(block, "simulation", u"").strip()

  if (not imported) and (not get(block, "top_level", False)) and (not len(sim_files)):
    print "WARNING: block %s not simulated!" % name
  if (not imported) and (len(timings) or len(simulation)):
    assert len(sim_files)
    render_sim = u"\n\n".join(render_simulations(name, sim_files, timings))
    put(ur'''
\paragraph{Simulació}

\begin{center}
  %s
\end{center}

%s

  ''', render_sim, simulation or "% FIXME")

  put(ur'''
\vspace{1cm}
  ''')
  return output[0]

def render_simulations(name, sim_files, timings):
  result = []
  for i, timing in enumerate(timings):
    file = open(sim_files[i], "rb")
    vwf = file.read()
    file.close()
    vwf = vwf2tikz.parser.parse_vwf(vwf)
    options = vwf2tikz.process.default_options.copy()
    options["scale"] = vwf.header["GRID_PERIOD"] / (get(timing, "scale", 1.0) * 4.5)
    
    for start, length in timing["slices"]:
      max_length = vwf.header["SIMULATION_TIME"] / vwf.header["GRID_PERIOD"] - start
      length = min(length, max_length)
      if length > 12 and not get(timing, "force", False):
        print "WARNING: Simulation for %s too long (%d grids), cropping to %d" % (name, length, 12)
        length = 12
      options["viewport"] = (start * vwf.header["GRID_PERIOD"], (start + length) * vwf.header["GRID_PERIOD"])
      result.append(vwf2tikz.process.render_vwf(vwf, options))
  
  return result

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
