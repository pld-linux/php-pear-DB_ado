# Todo
# - pl summary/description
%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       ado
%define		_pearname	%{_class}_%{_subclass}
%define		_status		stable
Summary:	%{_pearname} - DB driver which use MS ADODB library
Name:		php-pear-%{_pearname}
Version:	1.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
# Source0-md5:	b8ebb28f035c5a9c29bc91047423c093
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_ado is a database independent query interface definition for
Microsoft's ADODB library using PHP's COM extension. This class allows
you to connect to different data sources like MS Access, MS SQL
Server, Oracle and other RDBMS on a Win32 operating system. Moreover
the possibility exists to use MS Excel spreadsheets, XML, text files
and other not relational data as data source.

This class has in PEAR status: %{_status}

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
