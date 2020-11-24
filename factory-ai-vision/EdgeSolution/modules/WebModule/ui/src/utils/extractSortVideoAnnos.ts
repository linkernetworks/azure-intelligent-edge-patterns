import * as R from 'ramda';

export const extractSortVideoAnnos = (annos: { id: string }[]) => {
  const propName = R.prop('id');

  const sortRes = R.sortWith([R.ascend(propName)])(annos);

  return sortRes;
};
