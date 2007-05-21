%define name     medit
%define version  0.6.98
%define release  %mkrel 1

Name:        %{name}
Version:     %{version}
Release:     %{release}
Summary:     Multiplatform GTK+2 text editor
Group:       Editors
License:     GPL
URL:         http://ggap.sourceforge.net/medit/
Source0:     http://prdownloads.sourceforge.net/ggap/%{name}-%{version}.tar.bz2
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:        libgtk+2.0_0 libxml2
BuildRequires:   gtk2-devel libxml2-devel

%description
Medit is a multiplatform GTK+2 text editor.
Features:
o Configurable syntax highlighting
o Configurable keyboard accelerators
o Multiplatform - works both on unix and windows 


%prep
%setup -q

%build
%configure2_5x \
     --with-xml \
     --without-pygtk \
     --without-python

%make

%install
rm -rf %buildroot
%makeinstall_std

# menu
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/medit" \
needs="x11" \
icon="editors_section.png" \
section="More Applications/Editors" \
title="Medit" \
longtitle="%summary"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/moo/*.cfg
%{_datadir}/moo/completion/*
%{_datadir}/moo/syntax/*
%{_datadir}/pixmaps/*
%{_libdir}/moo/plugins/*.py
%{_libdir}/moo/plugins/lib/*.py
%{_iconsdir}/hicolor/*/apps/medit.png

%_menudir/%name
