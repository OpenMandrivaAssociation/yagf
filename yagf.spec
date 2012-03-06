%define version 0.9
%define	rel	1
%define release %mkrel %{rel}

Summary: Yet Another Graphic Front-end for Cuneiform
Name: 		yagf
Version:	%{version}
Release:	%{release}
License: 	GPLv3+
Group: 		Office
URL: 		http://symmetrica.net/cuneiform-linux/yagf-en.html
Source: 	http://symmetrica.net/cuneiform-linux/yagf-%{version}.tar.gz
#Source1: 	http://symmetrica.net/cuneiform-linux/yagf-%{version}-qt.4.6.x.tar.gz
Patch0:		YAGF.desktop.patch
Patch1:		yagf-0.9-mdv-linkage.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: 	cmake, qt4-common, qt4-devel, aspell-devel djvulibre-devel tiff-devel
Requires: 	qt4-common, aspell, 
Suggests:	cuneiform-linux
Suggests:	tesseract
Requires:	aspell-ru, aspell-uk aspell-en

%description
YAGF is a graphical interface for cuneiform and tesseract text recognition
tools on the Linux platform. With YAGF you can scan images via XSane, import
pages from PDF documents, perform images preprocessing and recognize texts
using cuneiform from a single command center. YAGF also makes it easy to scan
and recognize several images sequentially.

%prep
#%if %mdkversion >= 201100
%setup -q -n %{name}-%{version}
#%else
#%setup -T -a 1 -q -n %{name}-%{version}-qt-4.6.x
#%endif

#patch0 -p0
%patch1 -p1

%build
%cmake
#cmake ./ -DCMAKE_INSTALL_PREFIX=/usr/
%make

%install
rm -rf %{buildroot}
pushd build
%makeinstall_std
popd

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_bindir}/yagf
%{_datadir}/yagf
%{_datadir}/pixmaps/yagf.png
%{_datadir}/icons/hicolor/*/apps/yagf.*
%{_libdir}/yagf/libxspreload.so
%{_datadir}/applications/YAGF.desktop
%doc AUTHORS ChangeLog DESCRIPTION README
