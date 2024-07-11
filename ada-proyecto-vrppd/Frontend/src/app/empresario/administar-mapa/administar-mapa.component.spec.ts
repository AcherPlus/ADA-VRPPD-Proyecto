import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdministarMapaComponent } from './administar-mapa.component';

describe('AdministarMapaComponent', () => {
  let component: AdministarMapaComponent;
  let fixture: ComponentFixture<AdministarMapaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdministarMapaComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdministarMapaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
