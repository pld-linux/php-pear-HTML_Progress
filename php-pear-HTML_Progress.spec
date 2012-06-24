%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Progress
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - including a loading bar in your XHTML documents quickly and easily
Summary(pl):	%{_pearname} - szybkie i �atwe do��czanie paska post�pu w dokumentach XHTML
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fdec29cbace172a2b4e7e0de256229b7
URL:		http://pear.php.net/package/HTML_Progress/
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
- create horizontal and also vertical bart
- optional message line come with progress status
- percent info is floating all around the progress bar
- scale can be changed (default is 100)
- legend of percent text info can be changed (default is "%")

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc� tego pakietu mo�na w �atwy spos�b doda� w pe�ni
konfigurowalny pasek post�pu w ju� istniej�cych dokumentach XHTML.

Przegl�darka powinna akcpetowa� DHTML.

Cechy:
- mo�liwo�� u�ywania ju� istniej�cych arkuszy CSS w celu okre�lenia
  rozmiaru i koloru
- mo�liwo�� zmiany kolor�w i rozmiar�w poszczeg�lnych element�w
- pokazanie lub ukrycie tekstowej informacji o post�pie
- ustawianie/dodawanie oraz zwracanie bie��cej informacji o post�pie
- kompatybilny ze wszystkimi standardami CSS/XHTML
- mo�liwa integracja z rodzin� szablon�w ITx
- tworzenie poziomych oraz pionowych pask�w post�pu
- opcjonalna linia z komunikatem w statusie post�pu
- procentowa informacja "p�ywa" dooko�a paska post�pu
- skala mo�e by� zmieniona (domy�lnie 100)
- legenda procentowej informacji tekstowej mo�e by� zmieniona
  (domy�lnie "%")

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Error/Raise

install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Error/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Error
install %{_pearname}-%{version}/Error/Raise/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Error/Raise

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{ChangeLog,examples,INSTALL,LICENSE,README,Release-*,tests,tutorials}
%{php_pear_dir}/%{_class}/%{_subclass}
