Name:		texlive-random
Version:	54723
Release:	2
Summary:	Generating "random" numbers in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/random
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/random.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/random.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Generates pseudo-random integers in the range 1 to 2^{31}.
Macros are to provide random integers in a given range, or
random dimensions which can be used to provide random `real'
numbers, are also available.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/random
%doc %{_texmfdistdir}/doc/generic/random

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
