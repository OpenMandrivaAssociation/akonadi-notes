Name:		akonadi-notes
Epoch:		3
Version:	17.03.80
Release:	1
Summary:	Akonadi Notes Integration
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://www.kde.org/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Akonadi) >= 5.3.1
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	boost-devel

%description
Akonadi Notes Integration.

#--------------------------------------------------------------------

%define major 5
%define libname %mklibname KF5AkonadiNotes %{major}

%package -n %{libname}
Summary:      Akonadi Notes Integration main library
Group:        System/Libraries
Obsoletes:	%{mklibname KF5AkonadiNotes 5} < 3:16.08.2

%description -n %{libname}
Akonadi Notes Integration main library.

%files -n %{libname}
%{_libdir}/libKF5AkonadiNotes.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname KF5AkonadiNotes -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KF5/Akonadi/Notes/
%{_includedir}/KF5/akonadi/notes/
%{_includedir}/KF5/*_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5AkonadiNotes/
%{_libdir}/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
