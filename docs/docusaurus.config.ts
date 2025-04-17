import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Moodle GIFT Конвертер',
  tagline: 'Легке перетворення питань із Word у формат Moodle',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://yuranebykov.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/docx-to-moodle-gift/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'yuranebykov', // Usually your GitHub org/user name.
  projectName: 'docx-to-moodle-gift', // Usually your repo name.

  deploymentBranch: 'gh-pages',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'uk',
    locales: ['uk'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Moodle GIFT Конвертер',
      logo: {
        alt: 'Moodle GIFT Конвертер Лого',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Документація',
        },
        {
          href: 'https://github.com/yuranebykov/docx-to-moodle-gift',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Документація',
          items: [
            {
              label: 'Початок роботи',
              to: '/docs/intro',
            },
            {
              label: 'Поширені запитання',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Додаткові',
          items: [            
            {
              label: 'Завантаження EXE',
              href: 'https://github.com/yuranebykov/docx-to-moodle-gift/releases/download/v1.0.0/docx-to-moodle-gift.exe',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/yuranebykov/docx-to-moodle-gift',
            },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Docx у GIFT. Створено з ❤️ за допомогою Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
