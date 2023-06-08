Name:		akonadi-notes
Epoch:		3
Version:	23.04.2
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
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%define major 5
%define oldlibname %mklibname KF5AkonadiNotes 5
%define libname %mklibname KPim5AkonadiNotes

Requires: %{libname} = %{EVRD}

%description
Akonadi Notes Integration.

%files -f akonadinotes5.lang

#--------------------------------------------------------------------

%package -n %{libname}
Summary:      Akonadi Notes Integration main library
Group:        System/Libraries
Obsoletes:	%{mklibname KF5AkonadiNotes 5} < 3:16.08.2
Requires:	%{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
Akonadi Notes Integration main library.

%files -n %{libname}
%{_libdir}/libKPim5AkonadiNotes.so.%{major}*

#--------------------------------------------------------------------

%define olddevelname %mklibname KF5AkonadiNotes -d
%define develname %mklibname KPim5AkonadiNotes -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}
%rename %{olddevelname}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim5/AkonadiNotes
%{_libdir}/*.so
%{_libdir}/cmake/KPim5AkonadiNotes/
%{_libdir}/cmake/KF5AkonadiNotes/
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadinotes5
