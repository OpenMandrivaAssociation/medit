Name:		medit
Version:	1.1.0
Release:	%mkrel 1
Summary:	Multiplatform GTK+2 text editor
Group:		Editors
License:	GPLv2+
URL:		http://mooedit.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mooedit/%{name}-%{version}.tar.bz2
Patch0:		medit-1.1.0-dso.patch
BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	libsm-devel
BuildRequires:	imagemagick

%description
Medit is a multiplatform GTK+2 text editor.
Features:
o Configurable syntax highlighting
o Configurable keyboard accelerators
o Multiplatform - works both on unix and windows

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-install-hooks
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# more icon sizes, 48x48 is already installed by make install
for size in 32x32 16x16; do
%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/$size/apps;
convert moo/mooutils/pixmaps/medit.png -scale $size %{buildroot}%{_iconsdir}/hicolor/$size/apps/%{name}.png;
done

%if %{mdvver} >= 2012
%find_lang medit-1 medit-1-gsv medit-1.lang
%else
%find_lang medit-1 medit-1-gsv
%endif

%clean
%__rm -rf %{buildroot}

%files -f medit-1.lang
%doc COPYING README
%doc %{_defaultdocdir}/medit-1
%{_bindir}/medit
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/medit.1.*
%{_datadir}/medit-1/



%changelog
* Fri Mar 23 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 786437
- New version 1.1.0, switch from cmake to autotools

* Wed Nov 03 2010 Funda Wang <fwang@mandriva.org> 0.10.5-1mdv2011.0
+ Revision: 592770
- BR cmake
- new version 0.10.5

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.9.4-2mdv2009.1
+ Revision: 320294
- rebuild for new python

* Sat Aug 30 2008 Funda Wang <fwang@mandriva.org> 0.9.4-1mdv2009.0
+ Revision: 277537
- New version 0.9.4

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.9.2-3mdv2009.0
+ Revision: 252270
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Jan 21 2008 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2008.1
+ Revision: 155675
- New version 0.9.2
- rediff patch0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 01 2007 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 114221
- New version 0.9.0

* Sat Nov 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.8.11-1mdv2008.1
+ Revision: 109208
- New release 0.8.11

* Tue Aug 07 2007 Funda Wang <fwang@mandriva.org> 0.8.10-1mdv2008.0
+ Revision: 59667
- New version 0.8.10

* Wed Aug 01 2007 Funda Wang <fwang@mandriva.org> 0.8.9-1mdv2008.0
+ Revision: 57568
- New version 0.8.9

* Thu Jul 12 2007 Funda Wang <fwang@mandriva.org> 0.8.8-1mdv2008.0
+ Revision: 51500
- Fix file list
- New version

* Thu Jun 14 2007 Funda Wang <fwang@mandriva.org> 0.8.6-1mdv2008.0
+ Revision: 39539
- SILent renew tarball
- New version
- New version
  add dirty patch that skips update-icon-cache and mime database when building

  + Jérôme Soyer <saispo@mandriva.org>
    - Import medit




* Tue May 09 2006 UTUMI Hirosi <utuhiro78@dummy.org> 0.6.98-1mdk
- new release

* Mon May 08 2006 UTUMI Hirosi <utuhiro78@dummy.org> 0.6.97-1mdk
- first spec for Mandriva
