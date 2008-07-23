%define name    camE
%define version 1.9
%define release %mkrel 6

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    A rewrite of the xawtv webcam app, which adds imlib2 support
License:    GPL
Group:      Video
Source:     http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.bz2
Patch:      %{name}-1.9-fix-curl-issue.patch
URL:        http://linuxbrit.co.uk/camE
BuildRequires:  giblib-devel
BuildRequires:  imlib2-devel
BuildRequires:  freetype-devel
BuildRequires:  curl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
camE is a rewrite of the xawtv webcam app, which adds imlib2 support and
thus many new possibilities.

%prep
%setup -q
%patch -p 1

%build
perl -pi -e 's/-O3 -g -Wall/\$(RPM_OPT_FLAGS) -DFALSE=0 -DTRUE=1/' Makefile
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING *.style example.camErc*
%{_bindir}/%{name}


