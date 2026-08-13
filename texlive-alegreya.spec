%global tl_name alegreya
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Alegreya fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/alegreya
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alegreya.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alegreya.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The Alegreya fonts are designed by Juan Pablo del Peral for Huerta
Tipografica. Alegreya is a typeface originally intended for literature.
It conveys a dynamic and varied rhythm which facilitates the reading of
long texts. The italic has just as much care and attention to detail in
the design as the roman. Bold, black, small caps and five number styles
are available.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from alegreya:
Map Alegreya.map
TL_DROPIN_EOF
