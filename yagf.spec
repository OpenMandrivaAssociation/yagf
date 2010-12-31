%define version 0.8.2
%define	rel	1
%define release %mkrel %{rel}

Summary: Yet Another Graphic Front-end for Cuneiform
Name: 		yagf
Version:	%{version}
Release:	%{release}
License: 	GPL3+
Group: 		Office
URL: 		http://symmetrica.net/cuneiform-linux/yagf-en.html

Source: 	http://symmetrica.net/cuneiform-linux/yagf-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	cmake, qt4-common >= 4.4.3, libqt4-devel, aspell-devel libdjvulibre-devel
Requires: 	qt4-common >= 4.4.3, aspell, cuneiform-linux, aspell-ru, aspell-uk aspell-en

%description
YAGF is a graphical front-end for cuneiform OCR tool.
With YAGF you can open already scanned image files or obtain new images via XSane (scanning results are automatically passed to YAGF).
Once you have a scanned image you can prepare it for recognition, select particular image areas for recognition, set the recognition language and so no.
Recognized text is displayed in a editor window where it can be corrected, saved to disk or copied to clipboard.  
YAGF also provides some facilities for a multi-page recognition (see the online help for more details).

%prep
%setup -q

%build
cmake ./ -DCMAKE_INSTALL_PREFIX=/usr/
%make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_bindir}/yagf
%{_datadir}/yagf/*
%{_datadir}/yagf/translations/*
%{_datadir}/pixmaps/yagf.png
%{_datadir}/icons/hicolor/96x96/apps/yagf.png
%{_libdir}/yagf/libxspreload.so
%{_datadir}/applications/YAGF.desktop
