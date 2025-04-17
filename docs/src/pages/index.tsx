import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">Перетворюй питання з Word у формат GIFT для Moodle — швидко, зручно, без болю.</p>
        <p>Мінімальні системні вимоги: Windows 10</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/getting-started">
            Початок роботи
          </Link>
          <Link
            className="button button--secondary button--lg"
            to="/docs/faq">
            Поширені запитання
          </Link>
          <Link
            className="button button--secondary button--lg"
            href='https://github.com/yuranebykov/docx-to-moodle-gift/releases/download/v1.0.0/docx-to-moodle-gift.exe'>
            Завантажити EXE
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      description={siteConfig.tagline}>
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
