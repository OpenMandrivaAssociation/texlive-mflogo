%global tl_name mflogo
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	LaTeX support for Metafont logo fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mflogo
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX package and font definition file to access the Knuthian mflogo
fonts described in 'The Metafontbook' and to typeset Metafont logos in
LaTeX documents.

