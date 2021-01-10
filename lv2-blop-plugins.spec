Summary:	Port of the BLOP LADSPA plugins to LV2
Summary(pl.UTF-8):	Port wtyczek LADSPA BLOP do LV2
Name:		lv2-blop-plugins
Version:	1.0.2
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/blop-lv2-%{version}.tar.bz2
# Source0-md5:	6c9688652dec5329ea06f99b657aa174
URL:		http://drobilla.net/software/blop-lv2/
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel >= 1.16.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 2
Requires:	lv2 >= 1.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
This is a port of the BLOP LADSPA plugins to LV2.

%description -l pl.UTF-8
Ten pakiet zawiera port wtyczek LADSPA BLOP do LV2.

%prep
%setup -q -n blop-lv2-%{version}

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%dir %{_libdir}/lv2/blop.lv2
%{_libdir}/lv2/blop.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/blop.lv2/*.so
