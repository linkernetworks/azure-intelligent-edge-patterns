import { Item as ImageListItem } from '../../ImageList';

export type MainImagesProps = {
  labeledImages: ImageListItem[];
  relabelImages: ImageListItem[];
  unlabeledImages: ImageListItem[];
  filteredCameras: string[];
  filteredParts: string[];
  imageAddedButNoAnno: boolean;
  labeledImagesLessThanFifteen: boolean;
  openCaptureDialog: () => void;
  onUpload: () => void;
};

export type UntaggedPivotProps = Pick<
  MainImagesProps,
  'relabelImages' | 'unlabeledImages' | 'filteredCameras' | 'filteredParts' | 'openCaptureDialog' | 'onUpload'
>;
