import React from 'react';

import { EmptyAddIcon } from '../EmptyAddIcon';

type ModelsProps = {
  onAddModelClick: () => void;
};

const Models: React.FC<ModelsProps> = ({ onAddModelClick }) => {
  return (
    <EmptyAddIcon
      subTitle="Add preexisting models"
      title="Add models"
      primary={{ text: 'Add a model', onClick: onAddModelClick }}
    />
  );
};

export default Models;
