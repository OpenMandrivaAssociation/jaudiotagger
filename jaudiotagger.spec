Name:		jaudiotagger
Version:	1.0.8
Release:	%mkrel 3
URL:		http://www.jthink.net/jaudiotagger/index.jsp
Summary:	Library for editing tags like ID3 in audio files such as MP3s
Group:		Development/Java
License:	LGPLv2+
Source:		%{name}v%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	java-devel java-rpmbuild ant
BuildRequires:	cobertura jakarta-oro junit ant-junit log4j asm
BuildArch:	noarch
%description
The aim of this project is to provide a world class Java library for
editing tag information in audio files, it currently supports Mp4 (Mp4,
M4p, M4a), Mp3 (id3v1,id3v2) and Ogg Vorbis.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}v%{version}
#TODO: rm *.jar
%{_bindir}/find . -name '*.jar' -or -name '*.class' -exec %{__rm} -f {} \;

#disable tests
%{__sed} -i 's/compile\.production,compile\.tests,run\.tests/compile.production/' build.xml

%build
ant build.jar

%install
%{__rm} -Rf %{buildroot}
%__install -d %{buildroot}%{_javadir}
%__install -m 0644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%__ln_s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%__install -d %{buildroot}%{_javadocdir}
%{__cp} -a www/javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%doc README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
