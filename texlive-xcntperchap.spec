Name:		texlive-xcntperchap
Version:	54080
Release:	2
Summary:	Track the number of subsections etc. that occur in a specified tracklevel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcntperchap
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcntperchap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcntperchap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is the successor of cntperchap and allows to
provide more tracklevels than just only one.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xcntperchap
%doc %{_texmfdistdir}/doc/latex/xcntperchap

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
