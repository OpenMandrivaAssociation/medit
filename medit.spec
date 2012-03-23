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

