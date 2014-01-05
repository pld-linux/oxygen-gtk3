Summary:	Oxygen-Gtk3 - a port of the default KDE widget theme (Oxygen), to gtk3
Name:		oxygen-gtk3
Version:	1.3.1
Release:	1
License:	LGPL v2.1
Group:		Themes/GTK+
Source0:	ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk3/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a8ca81ea29a93c5859f179266f07c66e
URL:		https://projects.kde.org/projects/playground/artwork/oxygen-gtk/
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oxygen-Gtk3 is a port of the default KDE widget theme (Oxygen)
to gtk3.

It's primary goal is to ensure visual consistency between gtk3 and
qt-based applications running under kde. A secondary objective is to
also have a stand-alone nice looking gtk3 theme that would behave well
on other Desktop Environments.

Unlike other attempts made to port the kde oxygen theme to gtk3, this
attempt does not depend on Qt (via some Qt to Gtk3 conversion engine),
nor does render the widget appearance via hard coded pixmaps, which
otherwise breaks everytime some setting is changed in kde.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.*/3.*.*/theming-engines/liboxygen-gtk.so
%dir %{_datadir}/themes/oxygen-gtk
%dir %{_datadir}/themes/oxygen-gtk/gtk-3.*
%{_datadir}/themes/oxygen-gtk/gtk-3.*/argb-apps.conf
%{_datadir}/themes/oxygen-gtk/gtk-3.*/icons4
%{_datadir}/themes/oxygen-gtk/gtk-3.*/kdeglobals
%{_datadir}/themes/oxygen-gtk/gtk-3.*/oxygenrc
%{_datadir}/themes/oxygen-gtk/gtk-3.*/*.css
%dir %{_datadir}/themes/oxygen-gtk/gtk-3.*/special-icons
%{_datadir}/themes/oxygen-gtk/gtk-3.*/special-icons/standardbutton-closetab-16.png
%{_datadir}/themes/oxygen-gtk/gtk-3.*/special-icons/standardbutton-closetab-down-16.png
%{_datadir}/themes/oxygen-gtk/gtk-3.*/special-icons/standardbutton-closetab-hover-16.png
