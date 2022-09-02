Summary:	Port of the BLOP LADSPA plugins to LV2
Summary(pl.UTF-8):	Port wtyczek LADSPA BLOP do LV2
Name:		lv2-blop-plugins
Version:	1.0.4
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/blop-lv2-%{version}.tar.xz
# Source0-md5:	379e0d924de0fd603a7567e5b66371ea
URL:		http://drobilla.net/software/blop-lv2/
BuildRequires:	lv2-devel >= 1.16.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%dir %{_libdir}/lv2/blop.lv2
%{_libdir}/lv2/blop.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/blop.lv2/*.so
