%define oname fssm

Name:       rubygem-%{oname}
Version:    0.1.4
Release:    %mkrel 1
Summary:    File System State Monitor
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/ttilley/fssm
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch

%description
file system state monitor


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/example.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/profile/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.markdown
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION.yml
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
