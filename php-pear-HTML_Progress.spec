%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Progress
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} How to include a loading bar in your XHTML documents quickly and easily
Summary(pl):	%{_pearname} Jak szybko i �atwo do��czy� pasek post�pu w dokumentach XHTML
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9cb056fda9df4e89df3fb3fe5eb1095c
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a way to add a loading bar fully costomizable in
existing XHTML documents.

Your browser should accept DHTML feature.

Features:
- allows usage of an existing stylesheet for colors and size model
- all colors and size elements are customizable
- show or hide text percent information
- set/add and returns value of current status of progress
- compliant with all CSS/XHTML standards
- integration with template engine ITx family is possible

This class has in PEAR status: %{_status}.

%description -l pl
Za pomoc� tego pakietu mo�na w �atwy spos�b doda� w pe�ni
konfigurowywalny pasek post�pu w ju� istniej�cych dokumentach XHTML.

Przegl�darka powinna akcpetowa� DHTML.

Cechy:
- mo�liwo�� u�ywania ju� istniej�cych arkuszy CSS w celu okre�lenia
  rozmiaru i koloru
- mo�liwo�� zmiany kolor�w i rozmiar�w poszczeg�lnych element�w
- pokazanie lub ukrycie tekstowej informacji o post�pie
- ustawianie/dodawanie oraz zwracanie bi�acej informacji o post�pie
- kompatybilny ze wszystkimi standardami CSS/XHTML
- mo�liwa integracja z rodzin� szablon�w ITx

Ta klasa ma w PEAR status: %{_status}.

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
%doc %{_pearname}-%{version}/{ChangeLog,docs,examples,INSTALL,LICENSE,README,Release-0.4.2,Release-0.4.1}
%{php_pear_dir}/%{_class}/*.php
