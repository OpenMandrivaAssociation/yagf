%define version 0.8.2
%define	rel	1
%define release %mkrel %{rel}
%define distsuffix edm

%{?dist: %{expand: %%define %dist 1}}

Summary: Yet Another Graphic Front-end for Cuneiform
Summary:ru Графическая оболочка для Cuneiform OCR
Summary:uk Графічна оболонка для Cuneiform OCR
Name: 		yagf
Version:	%{version}
Release:	%{release}
License: 	GPL3+
Group: 		Applications/Office
URL: 		http://symmetrica.net/cuneiform-linux/yagf-en.html

Packager: 	Dmitry Nikitin <luckas_fb@mail.ru>
Vendor: 	Andrei Borovsky
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
Authors:
--------
    Andrei Borovsky <anb@symmetrica.net>
%description -l ru
Графический интерфейс для консольной программы распознавания тектов cuneiform на платформе Linux.
Кроме того, YAGF позволяет управлять сканированием изображений, их предварительной обработкой и собственно распознаванием из единого центра. 
Программа YAGF также упрощает последовательное распознавание большого числа отсканированных страниц. 

%description -l uk
Графичічний інтерфейс для консольної програми розпізнавання тектів cuneiform на платформі Linux.
Крім цього, YAGF дозволяє керувати скануванням зображень, їх попередньою обробкою і разпізнаванням із єдиного центру. 
Програма YAGF також спрощує послідовне розпізнанвання великої кількості відсканованих сторінок.

%prep
%setup -q

%build
cmake ./ -DCMAKE_INSTALL_PREFIX=/usr/
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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

