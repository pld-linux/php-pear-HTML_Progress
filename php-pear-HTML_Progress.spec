%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Progress
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - including a loading bar in your XHTML documents quickly and easily
Summary(pl):	%{_pearname} - szybkie i �atwe do��czanie paska post�pu w dokumentach XHTML
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	1.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3c172a82bba9c2900b3d6d19b38d10ff
URL:		http://pear.php.net/package/HTML_Progress/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	Smarty
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude Smarty and optional dependencies and tests (HTML_TestListener.php, TestUnit.php)
%define		_noautoreq	'pear(Smarty.class.php)' 'pear(PEAR.*)' 'pear(HTML/QuickForm.*)' 'pear(HTML/QuickForm/Controller.*)' 'pear(Image/Color.*)' 'pear(HTML/Page2.*)' 'pear(HTML/Template/IT.*)' 'pear(HTML/Template/Sigma.*)' 'pear(Log.*)' 'pear(Config.*)' 'pear(HTML_TestListener.php)' 'pear(TestUnit.php)'

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
- legend of percent text info can be changed (default is "%%")

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc� tego pakietu mo�na w �atwy spos�b doda� w pe�ni
konfigurowalny pasek post�pu w ju� istniej�cych dokumentach XHTML.

Przegl�darka powinna akceptowa� DHTML.

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
  (domy�lnie "%%")

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/%{_pearname}/{ChangeLog,examples,HISTORY,INSTALL,LICENSE,README,Release-*,docs}
%{php_pear_dir}/%{_class}/%{_subclass}.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/tests/*
