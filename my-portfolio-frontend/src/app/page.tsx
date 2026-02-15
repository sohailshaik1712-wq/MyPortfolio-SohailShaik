import Image from "next/image";
import Link from "next/link";
import {
  Github,
  Linkedin,
  FileText,
  Lightbulb,
  MapPin,
  Building2,
} from "lucide-react";

const experiences = [
  {
    role: "System Engineer — Data Platform / MDM Engineer",
    company: "Tata Consultancy Services",
    client: "Diageo",
    period: "June 2024 – Present",
    highlights: [
      "Engineered scalable data pipelines and automated workflows using modular programming principles",
      "Built REST API integrations and backend services in Java/JS used across enterprise systems",
      "Applied algorithmic business rules for validation, transformation, and enrichment of large datasets",
      "Collaborated with cross-functional teams in Agile environment to deliver enterprise solutions",
    ],
  },
];

const socials = [
  {
    icon: Github,
    label: "GitHub",
    href: "https://github.com/sohailshaik1712-wq",
  },
  {
    icon: Linkedin,
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/sohailshaik1107/",
  },
  {
    icon: Lightbulb,
    label: "LeetCode",
    href: "https://leetcode.com/u/shaiksohail_1107/",
  },
  {
    icon: FileText,
    label: "Resume",
    href: "/Sohail-Shaik-Resume.pdf",
  },
];

const skills = {
  Languages: ["Python", "Java", "JavaScript", "SQL"],
  Databases: ["PostgreSQL", "MySQL", "SQLite"],
  Frameworks: ["FastAPI", "Django", "Streamlit"],
  DevOps: ["Docker", "Git", "Kafka", "CI/CD"],
};

const education = [
  {
    degree: "Bachelor of Technology",
    field: "Electronics and Communication Engineering",
    institution: "VNR VJIET",
    score: "8.42 CGPA",
    period: "2020 – 2024",
  },
  {
    degree: "Senior Secondary Education",
    field: "Science Stream",
    institution: "Sri Chaitanya Junior College",
    score: "9.63 GPA",
    period: "2018 – 2020",
  },
  {
    degree: "Secondary Education",
    field: "Science",
    institution: "Vishwabharati High School",
    score: "9.80 GPA",
    period: "2017 – 2018",
  },
];

const certifications = [
  {
    title: "Machine Learning",
    issuer: "Coursera | Stanford",
    year: "2023",
    credentialUrl:
      "https://www.coursera.org/account/accomplishments/specialization/UCX4VK7H22A4",
  },
  {
    title: "Machine Learning with Python",
    issuer: "Cognitive Class - IBM",
    year: "2023",
    credentialUrl:
      "https://courses.cognitiveclass.ai/certificates/2efd0f37d75846af83748dba280968da",
  },
  {
    title: "Databases and SQL for Data Science with Python",
    issuer: "Coursera - IBM",
    year: "2023",
    credentialUrl:
      "https://www.coursera.org/account/accomplishments/verify/FVK729TNTPHU",
  },
  {
    title: "Data Analysis with Python",
    issuer: "Coursera - IBM",
    year: "2023",
    credentialUrl:
      "https://www.coursera.org/account/accomplishments/verify/9Z7YBZ8H7GXA",
  },
];

export default function Home() {
  return (
    <div className="min-h-screen transition-colors duration-300">

      {/* Hero */}
      <section className="border-b border-[#e5e5ea] dark:border-[#2c2c2e]">
        <div className="max-w-6xl mx-auto px-6 py-32">
          <div className="grid lg:grid-cols-[2fr,1fr] gap-20 items-start">

            {/* Left */}
            <div>
              <h1 className="text-6xl md:text-7xl font-light tracking-tight mb-8">
                Sohail Shaik
              </h1>

              <p className="text-2xl text-[#6e6e73] dark:text-[#a1a1a6] mb-12">
                Data Platform Engineer at Tata Consultancy Services
              </p>

              <div className="space-y-6 mb-14 max-w-2xl text-[#6e6e73] dark:text-[#a1a1a6] leading-relaxed">
                <p>
                  I specialize in Master Data Management and data platform engineering,
                  building governed, analytics-ready pipelines for enterprise systems.
                </p>
                <p>
                  I also architect cloud-native applications focused on CI/CD,
                  FastAPI optimization, and scalable production systems.
                </p>
              </div>

              <div className="flex items-center gap-8 mb-12 text-sm text-[#6e6e73] dark:text-[#a1a1a6]">
                <div className="flex items-center gap-2">
                  <MapPin size={14} />
                  Hyderabad, India
                </div>
                <div className="flex items-center gap-2">
                  <Building2 size={14} />
                  Open to Opportunities
                </div>
              </div>

              {/* Buttons */}
              <div className="flex gap-4 mb-14">
                <Link
                  href="/projects"
                  className="px-6 py-3 bg-[#0071e3] text-white rounded-full text-sm font-medium hover:bg-[#0066cc] transition"
                >
                  View Projects
                </Link>

                <a
                  href="mailto:sohailshaik1712@gmail.com"
                  className="px-6 py-3 rounded-full border border-[#e5e5ea] dark:border-[#2c2c2e] text-sm hover:opacity-80 transition"
                >
                  Get in Touch
                </a>
              </div>

              {/* Social */}
              <div className="flex items-center gap-6">
                {socials.map(({ icon: Icon, label, href }) => (
                  <div key={label} className="relative group">
                    <a
                      href={href}
                      target="_blank"
                      rel="noopener noreferrer"
                      aria-label={label}
                      className="w-10 h-10 flex items-center justify-center rounded-full border border-[#e5e5ea] dark:border-[#2c2c2e] hover:bg-[#f5f5f7] dark:hover:bg-[#2c2c2e] transition"
                    >
                      <Icon size={18} />
                    </a>

                    <span className="absolute top-full mt-3 whitespace-nowrap rounded-md bg-[#1c1c1e] text-white dark:bg-white dark:text-[#1c1c1e] text-xs px-3 py-1 opacity-0 group-hover:opacity-100 transition">
                      {label}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Right */}
            <div>
              <div className="relative w-full aspect-square max-w-sm mx-auto">
                <div className="relative w-full h-full rounded-full overflow-hidden border border-[#e5e5ea] dark:border-[#2c2c2e] shadow-[0_20px_60px_rgba(0,0,0,0.08)] dark:shadow-[0_20px_60px_rgba(0,0,0,0.5)]">
                  <Image
                    src="/pic_sohail.jpeg"
                    alt="Sohail Shaik"
                    fill
                    className="object-cover"
                    priority
                  />
                </div>
              </div>

              <div className="grid grid-cols-3 gap-10 mt-14 text-center">
                <Stat label="Years" value="1.4+" />
                <Stat label="CGPA" value="8.42" />
                <Stat label="Focus" value="MLOps" />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Experience */}
      <Section title="Experience">
        <div className="relative pl-10">

          {/* Vertical Line */}
          <div className="absolute left-4 top-2 bottom-2 w-px bg-[#e5e5ea] dark:bg-[#2c2c2e]" />

          {experiences.map((exp, idx) => (
            <div key={idx} className="relative mb-14">

              {/* Timeline Dot */}
              <span className="absolute -left-[1.6rem] top-2 w-3 h-3 rounded-full bg-[#0071e3] dark:bg-[#2997ff] shadow-md" />

              <h3 className="text-xl font-medium mb-2">
                {exp.role}
              </h3>

              <p className="text-sm text-[#6e6e73] dark:text-[#a1a1a6] mb-6">
                {exp.company} · {exp.period}
              </p>

              <ul className="space-y-3 text-[#6e6e73] dark:text-[#a1a1a6]">
                {exp.highlights.map((h, i) => (
                  <li key={i} className="leading-relaxed">
                    {h}
                  </li>
                ))}
              </ul>

            </div>
          ))}
        </div>
      </Section>


      {/* Skills */}
      <Section title="Technical Skills">
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-12">
          {Object.entries(skills).map(([category, items]) => (
            <div key={category}>
              <h3 className="text-sm uppercase tracking-wide text-[#8e8e93] dark:text-[#a1a1a6] mb-6">
                {category}
              </h3>
              <ul className="space-y-3">
                {items.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </Section>

      {/* Certifications */}
      <Section title="Certifications">
        <div className="grid md:grid-cols-2 gap-10">
          {certifications.map((cert, idx) => (
            <a
              key={idx}
              href={cert.credentialUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="surface rounded-3xl p-8 hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(0,0,0,0.08)] dark:hover:shadow-[0_12px_40px_rgba(0,0,0,0.4)] transition-all duration-300"
            >
              <h3 className="text-lg font-medium mb-4">{cert.title}</h3>
              <p className="text-sm text-[#6e6e73] dark:text-[#a1a1a6] mb-2">
                {cert.issuer}
              </p>
              <p className="text-sm text-[#6e6e73] dark:text-[#a1a1a6]">
                {cert.year}
              </p>
            </a>
          ))}
        </div>
      </Section>

      {/* Education */}
      <Section title="Education">
        <div className="relative pl-10">

          {/* Vertical Line */}
          <div className="absolute left-4 top-2 bottom-2 w-px bg-[#e5e5ea] dark:bg-[#2c2c2e]" />

          {education.map((edu, idx) => (
            <div key={idx} className="relative mb-12">

              {/* Timeline Dot (more subtle than experience) */}
              <span className="absolute -left-[1.6rem] top-2 w-2.5 h-2.5 rounded-full bg-[#8e8e93] dark:bg-[#636366]" />

              <h3 className="text-lg font-medium mb-2">
                {edu.degree}
              </h3>

              <p className="text-sm text-[#6e6e73] dark:text-[#a1a1a6] mb-1">
                {edu.institution} · {edu.period}
              </p>

              <p className="text-sm text-[#6e6e73] dark:text-[#a1a1a6]">
                {edu.field} · {edu.score}
              </p>

            </div>
          ))}
        </div>
      </Section>


      {/* CTA */}
      <section className="border-t border-[#e5e5ea] dark:border-[#2c2c2e]">
        <div className="max-w-6xl mx-auto px-6 py-32 text-center">
          <h2 className="text-4xl font-light mb-8">Let’s work together</h2>
          <p className="text-[#6e6e73] dark:text-[#a1a1a6] mb-12 max-w-2xl mx-auto">
            I’m exploring opportunities in data engineering, MLOps,
            and cloud-native systems.
          </p>

          <Link
            href="/projects"
            className="inline-block px-8 py-3 bg-[#0071e3] text-white rounded-full text-sm font-medium hover:bg-[#0066cc] transition"
          >
            View My Work
          </Link>
        </div>
      </section>
    </div>
  );
}

function Section({ title, children }: any) {
  return (
    <section className="border-t border-[#e5e5ea] dark:border-[#2c2c2e]">
      <div className="max-w-6xl mx-auto px-6 py-32">
        <h2 className="text-3xl font-light mb-14">{title}</h2>
        {children}
      </div>
    </section>
  );
}

function Stat({ label, value }: any) {
  return (
    <div>
      <p className="text-2xl font-light">{value}</p>
      <p className="text-xs text-[#6e6e73] dark:text-[#a1a1a6]">
        {label}
      </p>
    </div>
  );
}
