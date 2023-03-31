Name:		texlive-zwgetfdate
Version:	15878
Release:	2
Summary:	Get package or file date
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zwgetfdate
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
