Summary: Yet Another Graphic Front-end for Cuneiform
Name: 		yagf
Version:	0.9.2
Release:	%mkrel 1
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
%setup -q

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


%changelog
* Sun Sep 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.2-1mdv2012.0
+ Revision: 816672
- update to 0.9.2

* Sun Apr 22 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.1-1
+ Revision: 792700
- update to 0.9.1
- remove exessive reqs

* Tue Mar 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9-1
+ Revision: 782515
- new version 0.9

  + Александр Казанцев <kazancas@mandriva.org>
    - enables YAGF to recognise German and Swedish text in Gothic typesetting (tesseract 3.0 or higher is required).

* Wed Jan 04 2012 Александр Казанцев <kazancas@mandriva.org> 0.8.9-1
+ Revision: 752688
- new version 0.8.9
- drop support qt 4.6
- fix spec

* Fri Sep 02 2011 Александр Казанцев <kazancas@mandriva.org> 0.8.7-1
+ Revision: 697780
- new version 0.8.7. Add tesseract support.

  + Sergey Zhemoitel <serg@mandriva.org>
    - patch russian comment in .desktop
    - patch russian comments in .desktop
    - patch russian comments in .desktop

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.8.6-2
+ Revision: 640474
- rebuild to obsolete old packages

* Tue Feb 22 2011 Александр Казанцев <kazancas@mandriva.org> 0.8.6-1
+ Revision: 639298
- new version 0.8.6

* Fri Jan 28 2011 Александр Казанцев <kazancas@mandriva.org> 0.8.5-1
+ Revision: 633710
- new version 0.8.5

* Wed Jan 05 2011 Александр Казанцев <kazancas@mandriva.org> 0.8.3-1mdv2011.0
+ Revision: 628930
- new version 0.8.3

* Fri Dec 31 2010 Александр Казанцев <kazancas@mandriva.org> 0.8.2-1mdv2011.0
+ Revision: 626911
- initial release
- import yagf


* Thu Apr 15 2010 Dmitry Nikitin <luckas_fb@mail.ru> - 0.8.2
- New version 0.8.2
- add support djvulibre by kinder
- add support for recognition format hocr and smarttext
- add Ukrainian translation for yagf
- update Russian translation
- some fix end of line

* Sun Aug 16 2009 Andrei Borovsky <anb@symmetrica.net> - 0.8.1
- batch recognition added
* Wed Aug 5 2009  Andrei Borovsky <anb@symmetrica.net> - 0.8.0
- text selection blocks are now resizable
- images management bar is added
* Wed Aug 5 2009  Andrei Borovsky <anb@symmetrica.net> - 0.8.0
- text selection blocks are now resizable
- images management bar is added
* Sat Jul 25 2009 Andrei Borovsky <anb@symmetrica.net> - 0.7.1
- scaling and rotation is kept between images in the series
- images and text may be scaled by Ctrl + mouse wheel or by Ctrl + [+]/[-] keys.
* Sun Jul 19 2009 Andrei Borovsky <anb@symmetrica.net> - 0.7.0
- spell-checking is added
- saving to html with images is added
* Fri Jul 17 2009 Andrei Borovsky <anb@symmetrica.net> - 0.6.2
- merged the patches with the appropriate files
- removed unnessesary ldconfig call
* Wed Jul 15 2009 Kyrill Detinov <lazy.kent.suse@gmail.com> - 0.6.1
- update to 0.6.1
- fixed build in x86-64
- corrected build requires
* Sat Jun 20 2009 Kyrill Detinov <lazy.kent.suse@gmail.com> - 0.5.0
- change compiling outside of the source tree
* Mon Jun 15 2009 Kyrill Detinov <lazy.kent.suse@gmail.com> - 0.5.0
- fix requires Qt version
* Mon Jun 08 2009 Kyrill Detinov <lazy.kent.suse@gmail.com> - 0.5.0
- correct build requires:  libqt4-devel <= 4.4.3, cmake >= 2.6
* Fri Jun 05 2009 Kyrill Detinov <lazy.kent.suse@gmail.com> - 0.5.0
- initial package created
