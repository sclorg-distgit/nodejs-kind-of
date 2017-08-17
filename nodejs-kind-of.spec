%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name kind-of

Summary:       Get the native type of a value.
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       3.0.2
Release:       7%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/kind-of
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Get the native type of a value.

What makes this so fast?

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.2-7
- rh-nodejs8 rebuild

* Wed Mar 08 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.2-6
- Add symlink macro

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.2-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.2-4
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.2-3
- Invoke find_provides_and_requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.2-2
- Enable scl macros

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com> - 2.0.1-1
- Initial package
