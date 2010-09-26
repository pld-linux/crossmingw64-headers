Summary:	Cross Mingw64 GNU development utilities - headers
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla Mingw64 - pliki nagłowkowe
Name:		crossmingw64-headers
Version:	1.0
Release:	0.1
License:	ZPL v2.1 with parts on Public Domain, BSD and LGPL.
Group:		Development/Tools
# svn co https://mingw-w64.svn.sourceforge.net/svnroot/mingw-w64/branches/releases/v1.0/mingw-w64-headers mingw64-headers
%define		_rev	3647
Source0:	mingw64-headers.tar.bz2
# Source0-md5:	900f8604d077d904f5236b89a88ed416
URL:		http://mingw-w64.sourceforge.net/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		x86_64-pc-mingw32
%define		arch		%{_prefix}/%{target}

%description
crossmingw64 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw64 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to x86_64-pc-mingw32,
along with supporting Win64 libraries in PE+ format from free sources.

This package contains cross targeted headers for Win64.

%description -l pl.UTF-8
crossmingw64 jest kompletnym systemem do skrośnej kompilacji,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw64. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy x86_64-pc-mingw32,
oraz z bibliotek w PE+.

Ten pakiet zawiera pliki nagłówkowe dla Win64.

%prep
%setup -q -n mingw64-headers
if [ "`svnversion -n`" != "%{_rev}" ]; then
	exit 1
fi

%build
./configure \
	--prefix=%{_prefix} \
	--build=%{_target_platform} \
	--host=%{target} \
	--with-sdk=all

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%{arch}/include
