%define		_status		stable
%define		_pearname	DB_ado
Summary:	%{_pearname} - DB driver which use MS ADODB library
Summary(pl.UTF-8):	%{_pearname} - sterownik DB używający biblioteki MS ADODB
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	49c0bcdcc75d2396336c876aff01220b
URL:		http://pear.php.net/package/DB_ado/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-com
Requires:	php-common >= 3:4.1
Requires:	php-pear
Requires:	php-pear-DB
BuildArch:	noarch
ExclusiveOS:	Windows
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_ado is a database independent query interface definition for
Microsoft's ADODB library using PHP's COM extension. This class allows
you to connect to different data sources like MS Access, MS SQL
Server, Oracle and other RDBMS on a Win32 operating system. Moreover
the possibility exists to use MS Excel spreadsheets, XML, text files
and other not relational data as data source.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
DB_ado to definicja niezależnego od bazy interfejsu zapytań dla
biblioteki Microsoft ADODB, używająca rozszerzenia PHP COM. Klasa ta
pozwala na łączenie się z różnymi źródłami danych, jak MS Access, MS
SQL Server, Oracle czy inne RDBMS na systemie operacyjnym Win32. Co
więcej, istnieje możliwość używania arkuszy MS Excela, XML-a, plików
tekstowych i innych nierelacyjnych danych jako źródeł danych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

rm $RPM_BUILD_ROOT%{php_pear_dir}/DB/test/ado_test.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/DB/ado.php
%{php_pear_dir}/DB/ado_constants.php
