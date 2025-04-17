import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: '🖱 Простий інтерфейс',
    description: (
      <>
        Зрозумілий та мінімалістичний інтерфейс — запускаєш і працюєш.
      </>
    ),
  },
  {
    title: '🧩 Візуальний редактор',
    description: (
      <>
        Переглядай і редагуй питання прямо у вікні програми.
      </>
    ),
  },
  {
    title: '💾 Збереження у TXT для Moodle',
    description: (
      <>
        Експортуй тести у форматі GIFT та імпортуй їх у Moodle за пару кліків.
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
