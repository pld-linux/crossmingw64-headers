Summary:	Cross MinGW-W64 GNU development utilities - headers
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla MinGW-W64 - pliki nagłówkowe
Name:		crossmingw64-headers
Version:	2.0
Release:	10
License:	ZPL v2.1 with parts on Public Domain, BSD and LGPL.
Group:		Development/Tools
# svn co https://mingw-w64.svn.sourceforge.net/svnroot/mingw-w64/stable/v2.x/mingw-w64-headers mingw64-headers
%define		_rev	5515
Source0:	mingw64-headers.tar.xz
# Source0-md5:	1268ff4bed4aab11c5604281f7741987
Patch0:		%{name}-stddef-max_align_t.patch
URL:		http://mingw-w64.sourceforge.net/
BuildRequires:	automake
BuildRequires:	subversion
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%define		target		x86_64-w64-mingw32
%define		archprefix	%{_prefix}/%{target}
%define		archincludedir	%{archprefix}/include

%description
crossmingw64 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW-W64 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to x86_64-pc-mingw32,
along with supporting Win64 libraries in PE32+ format from free
sources.

This package contains cross targeted headers for Win64.

%description -l pl.UTF-8
crossmingw64 jest kompletnym systemem do skrośnej kompilacji,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW-W64. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy x86_64-pc-mingw32,
oraz z bibliotek w formacie PE32+.

Ten pakiet zawiera pliki nagłówkowe dla Win64.

%prep
%setup -q -n mingw64-headers
svn upgrade
if [ "`svnversion -n`" != "%{_rev}" ]; then
	exit 1
fi
%patch -P0 -p1
cp -p include/ChangeLog ChangeLog.headers
cp -p direct-x/ChangeLog ChangeLog.direct-x-headers

%build
%{__aclocal}
%{__autoconf}
%{__automake}
./configure \
	--prefix=%{_prefix} \
	--build=%{_target_platform} \
	--host=%{target} \
	--enable-sdk=all

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog.direct-x-headers ChangeLog.headers
%{archincludedir}
