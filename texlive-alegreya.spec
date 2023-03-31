Name:		texlive-alegreya
Version:	64384
Release:	2
Summary:	Alegreya fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/alegreya
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alegreya.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alegreya.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
# For building OS level fonts
BuildRequires:	mkfontscale

%description
The Alegreya fonts are designed by Juan Pablo del Peral for
Huerta Tipografica. Alegreya is a typeface originally intended
for literature. It conveys a dynamic and varied rhythm which
facilitates the reading of long texts. The italic has just as
much care and attention to detail in the design as the roman.
Bold, black, small caps and five number styles are available.

%package -n fonts-ttf-alegreya
# Let's make it available for applications other than TeX too...
Summary:	Alegreya fonts
Group:		System/Fonts/True type

%description -n fonts-ttf-alegreya
The Alegreya fonts are designed by Juan Pablo del Peral for
Huerta Tipografica. Alegreya is a typeface originally intended
for literature. It conveys a dynamic and varied rhythm which
facilitates the reading of long texts. The italic has just as
much care and attention to detail in the design as the roman.
Bold, black, small caps and five number styles are available.

%files -n fonts-ttf-alegreya
%{_datadir}/fonts/OTF/alegreya

#-----------------------------------------------------------------------
%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/alegreya
%{_texmfdistdir}/fonts/map/dvips/alegreya
%{_texmfdistdir}/fonts/opentype/huerta/alegreya
%{_texmfdistdir}/fonts/tfm/huerta/alegreya
%{_texmfdistdir}/fonts/type1/huerta/alegreya
%{_texmfdistdir}/fonts/vf/huerta/alegreya
%{_texmfdistdir}/tex/latex/alegreya
%doc %{_texmfdistdir}/doc/fonts/alegreya

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

# Let's also make Alegreya available to the OS...
mkdir -p %{buildroot}%{_datadir}/fonts/OTF
cp -r fonts/opentype/huerta/alegreya %{buildroot}%{_datadir}/fonts/OTF/
cd %{buildroot}%{_datadir}/fonts/OTF/alegreya
mkfontscale .
