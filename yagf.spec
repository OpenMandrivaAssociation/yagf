%define version 0.9.1
%define	rel	1
%if %{mdvver} >=201100
%define release %rel
%else
%define release %mkrel %{rel}
%endif

Summary: Yet Another Graphic Front-end for Cuneiform
Name: 		yagf
Version:	%{version}
Release:	%{release}
License: 	GPLv3+
Group: 		Office
URL: 		http://symmetrica.net/cuneiform-linux/yagf-en.html
Source0: 	http://symmetrica.net/cuneiform-linux/yagf-%{version}.tar.gz
BuildRequires: 	cmake qt4-devel aspell-devel djvulibre-devel tiff-devel
#Requires: 	qt4-common aspell
Suggests:	cuneiform-linux
Suggests:	tesseract
#Requires:	aspell-ru aspell-uk aspell-en

%description
YAGF is a graphical interface for cuneiform and tesseract text recognition
tools on the Linux platform. With YAGF you can scan images via XSane, import
pages from PDF documents, perform images preprocessing and recognize texts
using cuneiform from a single command center. YAGF also makes it easy to scan
and recognize several images sequentially.

%prep
%setup -q -n %{name}

find . -type f -executable -exec chmod a-x {} \;

%build
%cmake
%make

%install
pushd build
%makeinstall_std
popd

%files
%{_bindir}/yagf
%{_datadir}/yagf
%{_datadir}/pixmaps/yagf.png
%{_datadir}/icons/hicolor/*/apps/yagf.*
%{_libdir}/yagf/libxspreload.so
%{_datadir}/applications/YAGF.desktop
%doc AUTHORS ChangeLog DESCRIPTION README
