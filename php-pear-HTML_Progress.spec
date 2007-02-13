%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Progress
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - including a loading bar in your XHTML documents quickly and easily
Summary(pl.UTF-8):	%{_pearname} - szybkie i łatwe dołączanie paska postępu w dokumentach XHTML
Name:		php-pear-%{_pearname}
Version:	1.2.5
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a068d4825f8254475dff662bf5814cef
Patch0:		%{name}-smarty.patch
URL:		http://pear.php.net/package/HTML_Progress/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2.1
Requires:	Smarty >= 2.6.10-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude Smarty and optional dependencies and tests (HTML_TestListener.php, TestUnit.php)
%define		_noautoreq	'pear(.*Smarty.class.php)' 'pear(PEAR.*)' 'pear(HTML/QuickForm.*)' 'pear(HTML/QuickForm/Controller.*)' 'pear(Image/Color.*)' 'pear(HTML/Page2.*)' 'pear(HTML/Template/IT.*)' 'pear(HTML/Template/Sigma.*)' 'pear(Log.*)' 'pear(Config.*)' 'pear(HTML_TestListener.php)' 'pear(TestUnit.php)'

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

%description -l pl.UTF-8
Za pomocą tego pakietu można w łatwy sposób dodać w pełni
konfigurowalny pasek postępu w już istniejących dokumentach XHTML.

Przeglądarka powinna akceptować DHTML.

Cechy:
- możliwość używania już istniejących arkuszy CSS w celu określenia
  rozmiaru i koloru
- możliwość zmiany kolorów i rozmiarów poszczególnych elementów
- pokazanie lub ukrycie tekstowej informacji o postępie
- ustawianie/dodawanie oraz zwracanie bieżącej informacji o postępie
- kompatybilny ze wszystkimi standardami CSS/XHTML
- możliwa integracja z rodziną szablonów ITx
- tworzenie poziomych oraz pionowych pasków postępu
- opcjonalna linia z komunikatem w statusie postępu
- procentowa informacja "pływa" dookoła paska postępu
- skala może być zmieniona (domyślnie 100)
- legenda procentowej informacji tekstowej może być zmieniona
  (domyślnie "%%")

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/{ChangeLog,examples,HISTORY,INSTALL,LICENSE,README,Release-*,docs}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
