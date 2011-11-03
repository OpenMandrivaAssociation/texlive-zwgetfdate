# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/zwgetfdate
# catalog-date 2008-08-24 14:29:08 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-zwgetfdate
Version:	20080824
Release:	1
Summary:	Get package or file date
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zwgetfdate
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package enables to fetch dates of used packages and files
and provide such information in macros. It is useful for
automatic obtaining the date of a package being documented,
mainly if you do not use doc/docstrip.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zwgetfdate/zwgetfdate.sty
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/License.txt
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/README
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/zwgetfdate.pdf
%doc %{_texmfdistdir}/doc/latex/zwgetfdate/zwgetfdate.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
