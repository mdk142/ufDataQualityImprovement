"""
Fix a bibtex file

Thomson Reuters Bibtex has several errors that violate bibtex sytax and choke
bibtex parsers.  These are:
  1.  Double brackets should be replaced with single brackets throughout.  For example,
      Thomson Reuters often uses Year = {{1988}}.  Should be Year = {1988}
  2.  All bibtex keywords must not contain blanks.  Thomson Reuters asserts
      Web of Science Category = {...}  All assertions should be changed to
      Web-of-Science-Category = {...}
      Meeting Abstract should be changed to Meeting-Abstract = {...}
  3.  The values for Funding-Acknowledgement often (about 30% of the time) include a
      meaningless escape sequence \{[}\} which confuses the parser.  This string of
      six characters should be replaced everywhere with a single space.

This program reads a bibtex file from stdin and writes and improved (the three errors above are repaired)
file to stdout

2012-08-25 MC Added additional publisher name corrections
"""
import sys
import fileinput
for line in fileinput.input():
    line = line.replace('ADIS INT LTD','ADIS INTERNATIONAL LIMITED')
    line = line.replace('AMER INST MATHEMATICAL SCIENCES','AMERICAN INSTITUTE OF MATHEMATICAL SCIENCES')
    line = line.replace('INST LOCAL SELF-GOVERNMENT PUBLIC PROCUREMENT MARIBOR','INSTITUTE OF LOCAL SELF-GOVERNMENT PUBLIC PROCUREMENT MARIBOR')
    line = line.replace('SAUDI THORACIC SOC','SAUDI THORACIC SOCIETY')
    line = line.replace('KOREAN NEUROLOGICAL ASSOC','KOREAN NEUROLOGICAL ASSOCIATION')
    line = line.replace('SOC APPLIED SPECTROSCOPY','SOCIETY FOR APPLIED SPECTROSCOPY')
    line = line.replace('AMER SOC NEPHROLOGY','AMERICAN SOCIETY OF NEPHROLOGY')
    line = line.replace('IVYSPRING INT PUBL','IVYSPRING INTERNATIONAL PUBLISHER')
    line = line.replace('KOREAN SOC APPLIED ENTOMOLOGY','KOREAN SOCIETY OF APPLIED ENTOMOLOGY')
    line = line.replace('SOC NUCLEAR MEDICINE INC','SOCIETY OF NUCLEAR MEDICINE INC')
    line = line.replace('UNIV CALIF','UNIVERSITY OF CALIFORNIA')
    line = line.replace('ENTOMOLOGICAL SOC BRASIL','ENTOMOLOGICAL SOCIETY OF BRASIL')
    line = line.replace('MEDKNOW PUBLICATIONS \& MEDIA PVT LTD','MEDKNOW PUBLICATIONS AND MEDIA PVT LTD')
    line = line.replace('UNIV LAVAL','UNIVERSITY LAVAL')
    line = line.replace('AMER SOC TROP MED \& HYGIENE','AMERICAN SOCIETY OF TROPICAL MEDICINE AND HYGIENE')
    line = line.replace('AUSTRALIAN PHYSIOTHERAPY ASSOC','AUSTRALIAN PHYSIOTHERAPY ASSOCIATION')
    line = line.replace('RADIOLOGICAL SOC NORTH AMERICA','RADIOLOGICAL SOCIETY OF NORTH AMERICA')
    line = line.replace('AMER FOLKLORE SOC','AMERICAN FOLKLORE SOCIETY')
    line = line.replace('INT BEE RESEARCH ASSOC','INTERNATIONAL BEE RESEARCH ASSOCIATION')
    line = line.replace('KOREAN SOC MECHANICAL ENGINEERS','KOREAN SOCIETY OF MECHANICAL ENGINEERS')
    line = line.replace('TEACHERS COLL OF COLUMBIA UNIV','TEACHERS COLLEGE OF COLUMBIA UNIVERSITY')
    line = line.replace('AMER BOARD FAMILY MEDICINE','AMERICAN BOARD OF FAMILY MEDICINE')
    line = line.replace('INST MATHEMATICAL STATISTICS','INSTITUTE OF MATHEMATICAL STATISTICS')
    line = line.replace('MICHIGAN STATE UNIV PRESS','MICHIGAN STATE UNIVERSITY PRESS')
    line = line.replace('MICROBIOLOGICAL SOCIETY KOREA','MICROBIOLOGICAL SOCIETY OF KOREA')
    line = line.replace('ACADEMIC PRESS LTD- ELSEVIER SCIENCE LTD','ACADEMIC PRESS')
    line = line.replace('BOTANICAL SOC AMER INC','BOTANICAL SOCIETY OF AMERICA, INC')
    line = line.replace('KOREAN METEOROLOGICAL SOC','KOREAN METEOROLOGICAL SOCIETY')
    line = line.replace('CHINESE INST ENGINEERS','CHINESE INSTITUTE OF ENGINEERS')
    line = line.replace('AMER ASSOC ADVANCEMENT SCIENCE','AMERICAN ASSOCIATION FOR THE ADVANCEMENT OF SCIENCE')
    line = line.replace('HOSOKAWA POWDER TECHNOL FOUNDATION','HOSOKAWA POWDER TECHNOLOGY FOUNDATION')
    line = line.replace('SOC BRASILEIRA ZOOLOGIA, UNIV FEDERAL PARANA','SOCIETY BRASILEIRA ZOOLOGIA, UNIVERSITY FEDERAL PARANA')
    line = line.replace('AMER MUSEUM NATURAL HISTORY','AMERICAN MUSEUM OF NATURAL HISTORY')
    line = line.replace('INT SCIENTIFIC LITERATURE, INC','INTERNATIONAL SCIENTIFIC LITERATURE, INC')
    line = line.replace('JOHN WILEY \& SONS INC','JOHN WILEY AND SONS INC')
    line = line.replace('NATL INST OCCUPATIONAL SAFETY \& HEALTH, JAPAN','NATIONAL INSTITUTE OF OCCUPATIONAL SAFETY AND HEALTH, JAPAN')
    line = line.replace('SOC BRASIL ENGENHARIA AGRICOLA','SOCIETY OF BRASIL ENGENHARIA AGRICOLA')
    line = line.replace('SOC CHILENA CIENCIA SUELO','SOCIETY OF CHILENA CIENCIA SUELO')
    line = line.replace('UNIV ILLINOIS PRESS','UNIVERSITY OF ILLINOIS PRESS')
    line = line.replace('ASME','AMERICAN SOCIETY OF MECHANICAL ENGINEERS')
    line = line.replace('GEOLOGICAL SOC AMER, INC','GEOLOGICAL SOCIETY OF AMERICA, INC')
    line = line.replace('NATL ASSOC BIOLOGY TEACHERS, INC','NATIONAL ASSOCIATION OF BIOLOGY TEACHERS, INC')
    line = line.replace('SOC STUDY REPRODUCTION','SOCIETY FOR THE STUDY OF REPRODUCTION')
    line = line.replace('UNIV HAWAII PRESS','UNIVERSITY OF HAWAII PRESS')
    line = line.replace('UNIV IOWA, COLL LAW','UNIVERSITY OF IOWA, COLLEGE LAW')
    line = line.replace('SOC BRASIL GENETICA','SOCIETY OF BRASIL GENETICA')
    line = line.replace('UNIV MINNESOTA PRESS','UNIVERSITY OF MINNESOTA PRESS')
    line = line.replace('AMER ASSOC CLINICAL ENDOCRINOLOGISTS','AMERICAN ASSOCIATION OF CLINICAL ENDOCRINOLOGISTS')
    line = line.replace('AMER SOC NEURORADIOLOGY','AMERICAN SOCIETY OF NEURORADIOLOGY')
    line = line.replace('EWHA WOMANS UNIV PRESS','EWHA WOMANS UNIVERSITY PRESS')
    line = line.replace('SOC VERTEBRATE PALEONTOLOGY','SOCIETY OF VERTEBRATE PALEONTOLOGY')
    line = line.replace('ACAD AMER FRANCISCAN HIST','ACADEMY OF AMERICAN FRANCISCAN HISTORY')
    line = line.replace('AMER SOC ICHTHYOLOGISTS \& HERPETOLOGISTS','AMERICAN SOCIETY OF ICHTHYOLOGISTS AND HERPETOLOGISTS')
    line = line.replace('CORWIN PRESS INC A SAGE PUBLICATIONS CO','SAGE PUBLICATIONS COMPANY')
    line = line.replace('EUROPEAN ASSOC AQUATIC MAMMALS','EUROPEAN ASSOCIATION FOR AQUATIC MAMMALS')
    line = line.replace('GIGA INST AFRICAN AFFAIRS','GIGA INSTITUTE OF AFRICAN AFFAIRS')
    line = line.replace('POLISH ACAD SCIENCES INST MATHEMATICS','INSTITUTE OF MATHEMATICS POLISH ACADEMY OF SCIENCES')
    line = line.replace('ACAD MANAGED CARE PHARMACY','ACADEMY OF MANAGED CARE PHARMACY')
    line = line.replace('INT ASSOC PLANT TAXONOMY-IAPT','INTERNATIONAL ASSOCIATION FOR PLANT TAXONOMY')
    line = line.replace('J ROSS PUBL','J ROSS PUBLISHING INC')
    line = line.replace('MINN LAW REVIEW FOUND','MINNESOTA LAW REVIEW FOUNDATION')
    line = line.replace('ARCHAEOLOGIES-JOURNAL OF THE WORLD ARCHAEOLOGICAL CONGRESS','ARCHAEOLOGIES- THE JOURNAL OF THE WORLD ARCHAEOLOGICAL CONGRESS')
    line = line.replace('AMER PSYCHIATRIC PUBLISHING, INC','AMERICAN PSYCHIATRIC PUBLISHING, INC')
    line = line.replace('INST CHEMICAL ENGINEERS','INSTITUTE OF CHEMICAL ENGINEERS')
    line = line.replace('AMER PUBLIC HEALTH ASSOC INC','AMERICAN PUBLIC HEALTH ASSOCIATION')
    line = line.replace('ASSOC COMPUTING MACHINERY','ASSOCIATION FOR COMPUTING MACHINERY')
    line = line.replace('JOURNAL PEDODONTICS INC','THE JOURNAL OF PEDODONTICS')
    line = line.replace('NATL TAX ASSOC','NATIONAL TAX ASSOCIATION')
    line = line.replace('AMER ACAD FAMILY PHYSICIANS','AMERICAN ACADEMY OF FAMILY PHYSICIANS')
    line = line.replace('AMER BAR ASSOC, ADMINISTRATIVE LAW \& REGULATORY PRACTICE SECTION','AMERICAN BAR ASSOCIATION')
    line = line.replace('A V S AMER INST PHYSICS','A V S AMERICAN INSTITUTE OF PHYSICS')
    line = line.replace('ASCE-AMER SOC CIVIL ENGINEERS','AMERICAN SOCIETY OF CIVIL ENGINEERS')
    line = line.replace('INT INFORMATION INST','INTERNATIONAL INFORMATION INSTITUTE')
    line = line.replace('MDPI AG','MULTIDISCIPLINARY DIGITAL PUBLISHING INSTITUTE AG')
    line = line.replace('UNIV NAPLES FEDERICO II','UNIVERSITY OF NAPLES FEDERICO II')
    line = line.replace('UNIV PENNSYLVANIA PRESS','UNIVERSITY OF PENNSYLVANIA PRESS')
    line = line.replace('EUROPEAN MATHEMATICAL SOC','EUROPEAN MATHEMATICAL SOCIETY')
    line = line.replace('FEDERATION AMER SOC EXP BIOL','FEDERATION OF AMERICAN SOCIETIES FOR EXPERIMENTAL BIOLOGY')
    line = line.replace('UNIV ANTIOQUIA, FAC CIENCIAS AGRARIAS','UNIVERSITY OF ANTIOQUIA, FAC CIENCIAS AGRARIAS')
    line = line.replace('GENETICS SOC AM','GENETICS SOCIETY OF AMERICA')
    line = line.replace('INST TRANSPORTATION ENGINEERS','INSTITUTE OF TRANSPORTATION ENGINEERS')
    line = line.replace('INT MEDICAL PRESS LTD','INTERNATIONAL MEDICAL PRESS LIMITED')
    line = line.replace('J RHEUMATOL PUBL CO','JOURNAL OF RHEUMATOLOGY PUBLISHING COMPANY')
    line = line.replace('NATL RECREATION PARK ASSOC','NATIONAL RECREATION AND PARK ASSOCIATION')
    line = line.replace('OXFORD UNIV PRESS INC','OXFORD UNIVERSITY PRESS INC')
    line = line.replace('SAUDI MED J','SAUDI MEDICAL JOURNAL')
    line = line.replace('SOC TEACHERS FAMILY MEDICINE','SOCIETY OF TEACHERS OF FAMILY MEDICINE')
    line = line.replace('AGRICULTURAL INSTITUTE CANADA','AGRICULTURAL INSTITUTE OF CANADA')
    line = line.replace('AMER ACAD AUDIOLOGY','AMERICAN ACADEMY OF AUDIOLOGY')
    line = line.replace('AMER ACAD PEDIATRICS','AMERICAN ACADEMY OF PEDIATRICS')
    line = line.replace('AMER ACAD SLEEP MEDICINE','AMERICAN ACADEMY OF SLEEP MEDICINE')  
    line = line.replace('AMERICAN ALLIANCE HEALTH PHYS EDUC REC AND DANCE','AMERICAN ALLIANCE FOR HEALTH, PHYSICAL EDUCATION, RECREATION AND DANCE')
    line = line.replace('AMER ASSOC ADVANCEMENT SCIENCE','AMERICAN ASSOCIATION FOR THE ADVANCEMENT OF SCIENCE')
    line = line.replace('AMER ASSOC CANCER RESEARCH','AMERICAN ASSOCIATION FOR CANCER RESEARCH')
    line = line.replace('AMER ASSOC CLINICAL CHEMISTRY','AMERICAN ASSOCIATION FOR CLINICAL CHEMISTRY')
    line = line.replace('AMER ASSOC COLL PHARMACY','AMERICAN ASSOCIATION OF COLLEGES OF PHARMACY')
    line = line.replace('AMER ASSOC IMMUNOLOGISTS','AMERICAN ASSOCIATION OF IMMUNOLOGISTS')
    line = line.replace('AMER ASSOC LABORATORY ANIMAL SCIENCE','AMERICAN ASSOCIATION OF LABORATORY ANIMAL SCIENCE')
    line = line.replace('AMER ASSOC LAW LIBRARIES','AMERICAN ASSOCIATION OF LAW LIBRARIES')
    line = line.replace('AMER ASSOC NEUROLOGICAL SURGEONS','AMERICAN ASSOCIATION OF NEUROLOGICAL SURGEONS')
    line = line.replace('AMER ASSOC PHYSICISTS MEDICINE AMER INST PHYSICS','AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE')
    line = line.replace('AMER ASSOC TEACHERS FRENCH','AMERICAN ASSOCIATION OF TEACHERS OF FRENCH')
    line = line.replace('AMER ASSOC TEACHERS SPANISH PORTUGUESE, INC','AMERICAN ASSOCIATION OF TEACHERS OF SPANISH AND PORTUGUESE')
    line = line.replace('AMER ASSOC ZOO VETERINARIANS','AMERICAN ASSOCIATION OF ZOO VETERINARIANS')
    line = line.replace('AMERICAN BOARD FAMILY MEDICINE','AMERICAN BOARD OF FAMILY MEDICINE')
    line = line.replace('AMER COLL PHYSICIANS','AMERICAN COLLEGE OF PHYSICIANS')
    line = line.replace('AMER COLL CHEST PHYSICIANS','AMERICAN COLLEGE OF CHEST PHYSICIANS')
    line = line.replace('AMER COLL VET PATHOLOGIST','AMERICAN COLLEGE OF VETERINARY PATHOLOGISTS')
    line = line.replace('AMER INST AERONAUT ASTRONAUT','AMERICAN INSTITUTE OF AERONAUTICS AND ASTRONAUTICS')
    line = line.replace('AMER INST BIOLOGICAL SCI','AMERICAN INSTITUTE OF BIOLOGICAL SCIENCE')
    line = line.replace('AMER INST MATHEMATICAL SCI','AMERICAN INSTITUTE OF MATHEMATICAL SCIENCES')
    line = line.replace('AMER INST PHYSICS','AMERICAN INSTITUTE OF PHYSICS')
    line = line.replace('AMER OCCUPATIONAL THERAPY ASSOC, INC','AMERICAN OCCUPATIONAL THERAPY ASSOCIATION')
    line = line.replace('AMER PSYCHIATRIC PUBLISHING, INC','AMERICAN PSYCHIATRIC PUBLISHING')
    line = line.replace('AMER PUBLIC HEALTH ASSOCIATION INC','AMERICAN PUBLIC HEALTH ASSOCIATION')
    line = line.replace('AMER SOC AGRICULTURAL \& BIOLOGICAL ENGINEERS','AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS')
    line = line.replace('AMER SOC AGRONOMY','AMERICAN SOCIETY OF AGRONOMY')
    line = line.replace('AMER SOC ANIMAL SCIENCE','AMERICAN SOCIETY OF ANIMAL SCIENCE')
    line = line.replace('AMER SOC BIOCHEMISTRY MOLECULAR BIOLOGY INC','AMERICAN SOCIETY OF BIOCHEMISTRY AND MOLECULAR BIOLOGY')
    line = line.replace('AMER SOC CLINICAL INVESTIGATION INC','AMERICAN SOCIETY FOR CLINICAL INVESTIGATION')    
    line = line.replace('AMER SOC CLINICAL ONCOLOGY','AMERICAN SOCIETY OF CLINICAL ONCOLOGY')
    line = line.replace('AMER SOC CLINICAL PATHOLOGY','AMERICAN SOCIETY FOR CLINICAL PATHOLOGY')
    line = line.replace('AMER SOC HEALTH-SYSTEM PHARMACISTS','AMERICAN SOCIETY OF HEALTH SYSTEM PHARMACISTS')
    line = line.replace('AMER SOC HEMATOLOGY','AMERICAN SOCIETY OF HEMATOLOGY')
    line = line.replace('AMER SOC HORTICULTURAL SCIENCE','AMERICAN SOCIETY FOR HORTICULTURAL SCIENCE')
    line = line.replace('AMER SOC ICHTHYOLOGISTS HERPETOLOGISTS','AMERICAN SOCIETY OF ICHTHYOLOGISTS AND HERPETOLOGISTS')
    line = line.replace('AMER SOC LIMNOLOGY OCEANOGRAPHY','ASSOCIATION FOR THE SCIENCES OF LIMNOLOGY AND OCEANOGRAPHY')
    line = line.replace('AMER SOC MICROBIOLOGY','AMERICAN SOCIETY FOR MICROBIOLOGY')
    line = line.replace('AMER SOC NUTRITIONAL SCIENCE','AMERICAN SOCIETY FOR NUTRITIONAL SCIENCE')
    line = line.replace('AMER SOC NUTRITION-ASN','AMERICAN SOCIETY FOR NUTRITION')
    line = line.replace('AMER SOC PHARMACOLOGY EXPERIMENTAL THERAPEUTICS','AMERICAN SOCIETY FOR PHARMACOLOGY AND EXPERIMENTAL THERAPEUTICS')
    line = line.replace('AMER SOC PLANT BIOLOGISTS','AMERICAN SOCIETY OF PLANT BIOLOGISTS')
    line = line.replace('AMER SOC PLANT TAXONOMISTS','AMERICAN SOCIETY OF PLANT TAXONOMISTS')
    line = line.replace('AMER SOC TESTING MATERIALS','ASTM INTERNATIONAL')
    line = line.replace('ANNALS FAMILY MEDICINE','ANNALS OF FAMILY MEDICINE')
    line = line.replace('ASCE-AMERICAN SOCIETY CIVIL ENGINEERS','AMERICAN SOCIETY OF CIVIL ENGINEERS')
    line = line.replace('ASME-AMERICAN SOCIETY MECHANICAL ENGINEERS','AMERICAN SOCIETY OF MECHANICAL ENGINEERS')   
    line = line.replace('ASSOCIATION COMPUTING MACHINERY','ASSOCIATION OF COMPUTING MACHINERY')
    line = line.replace('ASSOC EDUC JOURNALISM MASS COMMUNICATION','ASSOCIATION FOR EDUCATION IN JOURNALISM AND MASS COMMUNICATIONS')    
    line = line.replace('ASSOCIATION MILITARY SURGEONS US','ASSOCIATION OF MILITARY SURGEONS OF THE UNITED STATES')
    line = line.replace('ASSOC RESEARCH VISION OPHTHALMOLOGY INC','ASSOCIATION FOR RESEARCH IN VISION AND OPHTHALMOLOGY')
    line = line.replace('BOTANICAL SOCIETY AMERICAN INC','BOTANICAL SOCIETY OF AMERICA')
    line = line.replace('BRITISH INSTITUTE RADIOLOGY','BRITISH INSTITUTE OF RADIOLOGY')
    line = line.replace('CMA-CANADIAN MEDICAL ASSOC','CANADIAN MEDICAL ASSOCIATION')
    line = line.replace('CHURCHILL LIVINGSTONE INC MEDICAL PUBLISHERS','CHURCHILL LIVINGSTONE')
    line = line.replace('COLD SPRING HARBOR LAB PRESS, PUBLICATIONS DEPARTMENT','COLD SPRING HARBOR LABORATORY PRESS')
    line = line.replace('COLL AMER PATHOLOGISTS','COLLEGE OF AMERICAN PATHOLOGISTS')
    line = line.replace('COUNCIL EXCEPTIONAL CHILDREN','COUNCIL FOR EXCEPTIONAL CHILDREN')
    line = line.replace('CROP SCIENCE SOC AMER','CROP SCIENCE SOCIETY OF AMERICA')
    line = line.replace('CURRENT HIST INC','CURRENT HISTORY')
    line = line.replace('ECOLOGICAL SOC AMER','ECOLOGICAL SOCIETY OF AMERICA')
    line = line.replace('ENDOCRINESOC','THE ENDOCRINE SOCIETY')
    line = line.replace('ENTOMOLOGICAL SOC AMER','ENTOMOLOGICAL SOCIETY OF AMERICA')
    line = line.replace('FEDERATION AMER SOC EXP BIOL','FEDERATON OF AMERICAN SOCIETIES FOR EXPERIMENTAL BIOLOGY')
    line = line.replace('GERONTOLOGICAL SOC AMER','GERONTOLOGICAL SOCIETY OF AMERICA')
    line = line.replace('IEEE-INST ELECTRICAL ELECTRONICS ENGINEERS INC','INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS')
    line = line.replace('INST ENGINEERING TECHNOLOGY-IET','INSTITUTE OF ENGINEERING TECHNOLOGY')
    line = line.replace('JAPAN SOC VET SCI','JAPANESE SOCIETY OF VETERINARY SCIENCE')
    line = line.replace('JAPAN SOC APPLIED PHYSICS','JAPAN SOCIETY OF APPLIED PHYSICS')    
    line = line.replace('J O S P T','JOURNAL OF ORTHOPAEDIC & SPORTS PHYSICAL THERAPY')
    line = line.replace('JOURNAL FIELD ARCHEOLOGY','JOURNAL OF FIELD ARCHEOLOGY')
    line = line.replace('JOURNAL APPL BEHAV ANAL','JOURNAL OF APPLIED BEHAVIORAL ANALYSIS')
    line = line.replace('JOURNAL WUHAN UNIV TECHNOLOGY','JOURNAL OF THE WUHAN UNIVERSITY OF TECHNOLOGY')
    line = line.replace('MODERN HUMANITIES RES ASSN','MODERN HUMANITIES RESEARCH ASSOCIATION')
    line = line.replace('NATL ACAD SCIENCES','NATIONAL ACADEMY OF SCIENCES')
    line = line.replace('NATL ASSOC CORROSION ENG','NATIONAL ASSOCIATION OF CORROSION ENGINEERS')
    line = line.replace('NEOTROPICAL ORNITHOLOGICAL SOC, USGS PATUXENT WILDLIFE RESEARCH CTR','NEOTROPICAL ORNITHOLOGICAL SOCIETY')    
    line = line.replace('OPTICAL SOC AMER','OPTICAL SOCIETY OF AMERICA')
    line = line.replace('ORGANIZATION AMER HISTORIANS','ORGANIZATION OF AMERICAN HISTORIANS')
    line = line.replace('POLISH ACAD SCIENCES INST PHYSICS','POLISH ACADEMY OF SCIENCES INSTITUTE OF PHYSICS')
    line = line.replace('PUBLIC LIBRARY SCIENCE','PUBLIC LIBRARY OF SCIENCE')
    line = line.replace('ROSENSTIEL SCH MAR ATMOS SCI','THE ROSENSTIEL SCHOOL OF MARINE AND ATMOSPHERIC SCIENCE')
    line = line.replace('ROYAL SOC CHEMISTRY','ROYAL SOCIETY OF CHEMISTRY')
    line = line.replace('SOC AMER FORESTERS','SOCIETY OF AMERICAN FORESTERS')
    line = line.replace('SOC BRASILEIRA FITOPATOLOGIA','SOCIEDADE BRASILEIRA DE FITOPATOLOGIA')
    line = line.replace('SOC GENERAL MICROBIOLOGY','SOCIETY FOR GENERAL MICROBIOLOGY')
    line = line.replace('SOC NEMATOLOGISTS','SOCIETY OF NEMATOLOGISTS')
    line = line.replace('SOC NEUROSCIENCE','SOCIETY OF NEUROSCIENCE')
    line = line.replace('SOC STUDY AMPHIBIANS REPTILES','SOCIETY FOR THE STUDY OF AMPHIBIANS AND REPTILES')
    line = line.replace('SOC TEACHERS FAMILY MEDICINE','SOCIETY OF TEACHERS OF FAMILY MEIDCINE')
    line = line.replace('SOUTHERN APPALACHIAN BOTANICAL SOC, NEWBERRY COLL','SOUTHERN APPALACHIAN BOTANICAL SOCIETY')
    line = line.replace('SOIL SCI SOC AMER','SOIL SCIENCE SOCIETY OF AMERICA')
    line = line.replace('SPIE-SOC PHOTOPTICAL INSTRUMENTATION ENGINEERS','SOCIETY OF PHOTOPTICAL INSTRUMENTATION ENGINEERS')
    line = line.replace('UNIV CHICAGO PRESS','UNIVERSITY OF CHICAGO PRESS')
    line = line.replace('UNIV MARYLAND-CTR RENAISSANCE \& BAROQUE STUD','CENTER FOR RENAISSANCE AND BAROQUE STUDIES')
    line = line.replace('UNIV NEW MEXICO','UNIVERSITY OF NEW MEXICO')
    line = line.replace('UNIV TEHRAN','UNIVERSITY OF TEHRAN')
    line = line.replace('UROL \& NEPHROL RES CTR-UNRC','UROLOGY AND NEPHROLOGY RESEARCH CENTER')
    line = line.replace('WEED SCI SOC AMER','WEED SCIENCE SOCIETY OF AMERICA')
    line = line.replace('{{','{')
    line = line.replace('}}','}')
    line = line.replace("""``""",'"')
    line = line.replace("""{''}""",'"')
    line = line.replace(',}','}')
    line = line.replace('\&','and')
    line = line.replace('&','and')
    line = line.replace('Web of Science','Web-of-Science')
    line = line.replace('Meeting Abstract','Meeting-Abstract')
    line = line.replace('\{[}\}',' ')
    sys.stdout.write(line)

