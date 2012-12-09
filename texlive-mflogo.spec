# revision 17487
# category Package
# catalog-ctan /macros/latex/contrib/mflogo
# catalog-date 2010-03-14 23:46:18 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-mflogo
Version:	20100314
Release:	2
Summary:	LaTeX support for MetaFont logo fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mflogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX package and font definition file to access the Knuthian
mflogo fonts described in 'The MetaFontbook' and to typeset
MetaFont logos in LaTeX documents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logo10.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logo8.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logo9.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logobf10.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logod10.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logosl10.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logosl8.afm
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo/logosl9.afm
%{_texmfdistdir}/fonts/map/dvips/mflogo/mflogo.map
%{_texmfdistdir}/fonts/source/public/mflogo/flogo.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logo.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logo10.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logo8.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logo9.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logobf10.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logod10.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logosl10.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logosl8.mf
%{_texmfdistdir}/fonts/source/public/mflogo/logosl9.mf
%{_texmfdistdir}/fonts/source/public/mflogo/nlogo.mf
%{_texmfdistdir}/fonts/source/public/mflogo/sklogo.mf
%{_texmfdistdir}/fonts/tfm/public/mflogo/logo10.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logo8.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logo9.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logobf10.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logod10.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logosl10.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logosl8.tfm
%{_texmfdistdir}/fonts/tfm/public/mflogo/logosl9.tfm
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logo10.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logo8.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logo9.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logobf10.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logod10.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logosl10.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logosl8.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo/logosl9.pfb
%{_texmfdistdir}/tex/latex/mflogo/mflogo.sty
%{_texmfdistdir}/tex/latex/mflogo/ulogo.fd
%doc %{_texmfdistdir}/doc/latex/mflogo/mflogo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mflogo/CATALOGUE
%doc %{_texmfdistdir}/source/latex/mflogo/Makefile
%doc %{_texmfdistdir}/source/latex/mflogo/README
%doc %{_texmfdistdir}/source/latex/mflogo/mflogo.dtx
%doc %{_texmfdistdir}/source/latex/mflogo/mflogo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100314-2
+ Revision: 753935
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100314-1
+ Revision: 719008
- texlive-mflogo
- texlive-mflogo
- texlive-mflogo
- texlive-mflogo

