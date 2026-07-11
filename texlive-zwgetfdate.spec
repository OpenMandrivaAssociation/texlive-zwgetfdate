%global tl_name zwgetfdate
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Get package or file date
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zwgetfdate
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zwgetfdate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can fetch the date declaration of packages and files used by
a document, and then provide the information in macros. The facilities
provide a means of obtaining the date of a package being documented;
this is mainly of use when doc/docstrip.

