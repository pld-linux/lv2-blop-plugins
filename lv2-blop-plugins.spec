Summary:	Port of the BLOP LADSPA plugins to LV2
Summary(pl.UTF-8):	Port wtyczek LADSPA BLOP do LV2
Name:		lv2-blop-plugins
Version:	1.0.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/blop-lv2-%{version}.tar.bz2
# Source0-md5:	3dfd6f7366938a25a47d09d9dd863b8b
URL:		http://drobilla.net/software/blop-lv2/
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRequires:	python
Requires:	lv2 >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a port of the BLOP LADSPA plugins to LV2.

%description -l pl.UTF-8
Ten pakiet zawiera port wtyczek LADSPA BLOP do LV2.

%prep
%setup -q -n blop-lv2-%{version}

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
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
%doc AUTHORS README
%dir %{_libdir}/lv2/blop.lv2
%{_libdir}/lv2/blop.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/blop.lv2/*.so
