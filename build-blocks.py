#!/usr/bin/env python
# -*- coding: utf-8
# Render the contents for each block section in the specified
# project directory. Example: ./build-blocks.py 1A

from os import path, listdir, stat
from sys import argv
from runpy import run_path
import bdf2tikz.main, bdf2tikz.render

def escape(t):
  return bdf2tikz.render.render_tikz_text(t, {})

def get(o, n, d):
  if n in o: return o[n]
  return d

def render_block(name, block):
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

  # Schematic / VHDL and implementation
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
    ref = u"fig:\\projectname-%s" % name
    put(ur'''
\begin{figure}[b]
  \begin{center}
    \adjustbox{max width=\textwidth, max height=\textheight}{
      \bdfschematic{%s}
    }
  \end{center}
  \caption{\label{%s} Esquemàtic per al bloc \textsf{%s}}
\end{figure}

    ''', name, ref, escape(name))
    intro_text += u"L'esquemàtic del bloc es pot veure a la figura~\\ref{%s} (pàgina~\\pageref{%s}). " % (ref, ref)

  implementation = get(block, "implementation", "% FIXME")
  put(ur'''
%s

%s

  ''', intro_text.strip(), implementation.strip())

  # TODO: Simulation

  put(ur'''
\vspace{1cm}
  ''')
  return output[0]


project = argv[1]
pdir = path.join(path.dirname(__file__), project)
bdir = path.join(pdir, "blocks")
adir = path.join(pdir, "assets")
for block in listdir(bdir):
  name, ext = path.splitext(block)
  if ext != ".py": continue
  block = run_path(path.join(bdir, block))
  output = render_block(name, block)
  file = open(path.join(bdir, name + ".tex"), "w")
  file.write(output.encode("utf-8"))
  file.close()
