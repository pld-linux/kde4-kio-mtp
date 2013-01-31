#
# Conditional build:
#
%define		orgname		kio-mtp
%define		qtver		4.7.1
%define		kdever		4.9.0
%define         srcdate         20130121
Summary:	Media Transfer Protocol (MTP) kioslave
Summary(pl.UTF-8):	Media Transfer Protocol (MTP) kioslave
Name:		kde4-kio-mtp
Version:	0.0.%{srcdate}
Release:	0.1
License:	LGPL (GPL/GPL v2/GPL v2+... choose one)
Group:		X11/Applications
Source0:	http://beauty.ant.gliwice.pl/PLD/kio-mtp-20130121.tgz
# Source0-md5:	630c2ae98cd37963287ec73ee6e96ad5
URL:		http://www.afiestas.org/workspaces-gain-mtp-support/
# leave only required ones, note kde4-kdelibs-devel requires already a bunch full of them
#BuildRequires:	Qt3Support-devel >= %{qtver}
#BuildRequires:	QtCore-devel >= %{qtver}
#BuildRequires:	QtDBus-devel >= %{qtver}
#BuildRequires:	QtDesigner-devel >= %{qtver}
#BuildRequires:	QtGui-devel >= %{qtver}
#BuildRequires:	QtScript-devel >= %{qtver}
#BuildRequires:	QtSvg-devel >= %{qtver}
#BuildRequires:	QtTest-devel >= %{qtver}
#BuildRequires:	QtUiTools-devel >= %{qtver}
#BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kioslave which allows to manage files in any MTP capable device, like Android ones from KDE.

%description -l pl.UTF-8
Kioslave pozwalajacy zarzadzac plikami w urzadzeniach obslugujacych MTP, takich jak np Android z poziomu KDE.

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kio_mtp.so
%{_datadir}/apps/konqueror/dirtree/remote/mtp-network.desktop
%{_datadir}/apps/remoteview/mtp-network.desktop
%{_datadir}/apps/solid/actions/solid_mtp.desktop
%{_datadir}/kde4/services/mtp.protocol
