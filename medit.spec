%define name     medit
%define version  0.9.4
%define release  %mkrel 4

Name:        %{name}
Version:     %{version}
Release:     %{release}
Summary:     Multiplatform GTK+2 text editor
Group:       Editors
License:     GPLv2+
URL:         http://mooedit.sourceforge.net/
Source0:     http://prdownloads.sourceforge.net/mooedit/%{name}-%{version}.tar.bz2
Patch1:      medit-0.9.2-do-not-update-system-files.patch
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:   gtk2-devel libxml2-devel pcre-devel pygtk2.0-devel intltool

%description
Medit is a multiplatform GTK+2 text editor.
Features:
o Configurable syntax highlighting
o Configurable keyboard accelerators
o Multiplatform - works both on unix and windows


%prep
%setup -q
#patch1 -p1

%build
%configure2_5x \
     --enable-generated-files=no

%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang moo moo moo-gsv

%if %mdkversion < 200900
%post
%update_menus
%update_mime_database
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_mime_database
%clean_icon_cache hicolor
%endif

%clean
rm -rf %buildroot

%files -f moo.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/moo
%{_datadir}/pixmaps/*
%{_libdir}/moo
%{_iconsdir}/hicolor/*/apps/medit.png
%{_mandir}/man1/*
