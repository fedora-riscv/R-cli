%global packname  cli
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Helpers for Developing Command Line Interfaces

License:          MIT
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat R-crayon R-methods
# Suggests:  R-covr R-mockery R-testthat R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core

Requires:         R-assertthat
Requires:         R-crayon >= 1.3.4
Requires:         R-methods
BuildRequires:    R-devel tex(latex)
BuildRequires:    R-assertthat
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-methods
BuildRequires:    R-mockery R-testthat R-withr

%description
A suite of tools designed to build attractive command line interfaces
('CLIs'). Includes tools for drawing rules, boxes, trees, and 'Unicode'
symbols with 'ASCII' alternatives.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.0-1
- initial package for Fedora
