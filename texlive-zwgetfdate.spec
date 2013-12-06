# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/zwgetfdate
# catalog-date 2008-08-24 14:29:08 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-zwgetfdate
Version:	20080824
Release:	5
Summary:	Get package or file date
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zwgetfdate
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables to fetch dates of used packages and files
and provide such information in macros. It is useful for
automatic obtaining the date of a package being documented,
mainly if you do not use doc/docstrip.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zwgetfdate/zwgetfdate.sty
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/License.txt
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/README
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/zwgetfdate.pdf
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/zwgetfdate.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080824-2
+ Revision: 757785
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080824-1
+ Revision: 719976
- texlive-zwgetfdate
- texlive-zwgetfdate
- texlive-zwgetfdate

