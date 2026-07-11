%global tl_name random
%global tl_revision 54723

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Generating random numbers in TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/random
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/random.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/random.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Generates pseudo-random integers in the range 1 to 2^{31}. Macros are to
provide random integers in a given range, or random dimensions which can
be used to provide random `real' numbers, are also available.

