#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	chef-handler-slack
Summary:	Chef reports generated to a channel in Slack
Name:		ruby-%{pkgname}
Version:	0.1.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	a70cb20de7d0908e67796f4cbb2c4873
URL:		https://github.com/tinyspeck/chef-handler-slack
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-chef
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
Requires:	chef
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chef reports generated to a channel in Slack.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/chef/handler/slack.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
