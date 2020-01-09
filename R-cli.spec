%global packname  cli
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Helpers for Developing Command Line Interfaces

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat, R-crayon >= 1.3.4, R-glue, R-methods, R-utils, R-fansi
# Suggests:  R-callr, R-covr, R-htmlwidgets, R-knitr, R-mockery, R-rmarkdown, R-rstudioapi, R-prettycode >= 1.1.0, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core
Requires:         R-assertthat
Requires:         R-crayon >= 1.3.4
Requires:         R-glue
Requires:         R-methods
Requires:         R-utils
Requires:         R-fansi
Suggests:         R-callr
Suggests:         R-htmlwidgets
Suggests:         R-knitr
Suggests:         R-mockery
Suggests:         R-rmarkdown
Suggests:         R-rstudioapi
Suggests:         R-prettycode >= 1.1.0
Suggests:         R-testthat
Suggests:         R-withr
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-assertthat
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-glue
BuildRequires:    R-methods
BuildRequires:    R-utils
BuildRequires:    R-fansi
BuildRequires:    R-callr
BuildRequires:    R-htmlwidgets
BuildRequires:    R-knitr
BuildRequires:    R-mockery
BuildRequires:    R-rmarkdown
BuildRequires:    R-rstudioapi
BuildRequires:    R-prettycode >= 1.1.0
BuildRequires:    R-testthat
BuildRequires:    R-withr

%description
A suite of tools to build attractive command line interfaces ('CLIs'), from
semantic elements: headings, lists, alerts, paragraphs, etc. Supports custom
themes via a 'CSS'-like language. It also contains a number of lower level
'CLI' elements: rules, boxes, trees, and 'Unicode' symbols with 'ASCII'
alternatives. It integrates with the 'crayon' package to support 'ANSI'
terminal colors.


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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/logo.txt
%{rlibdir}/%{packname}/scripts


%changelog
* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.0-1
- initial package for Fedora
