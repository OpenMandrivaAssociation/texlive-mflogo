Epoch:		1
Name:		texlive-mflogo
Version:	42428
Release:	2
Summary:	LaTeX support for Metafont logo fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mflogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX package and font definition file to access the Knuthian
mflogo fonts described in 'The Metafontbook' and to typeset
Metafont logos in LaTeX documents.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/mflogo
%{_texmfdistdir}/fonts/tfm/public/mflogo
%{_texmfdistdir}/tex/latex/mflogo
%doc %{_texmfdistdir}/doc/latex/mflogo
#- source
%doc %{_texmfdistdir}/source/latex/mflogo

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
